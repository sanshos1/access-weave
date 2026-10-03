'use client';

import {useEffect, useState} from 'react';
import {connect, read, write} from '../lib/chain';

type Journey = {id: string; need: string; constraints: string[]; segments: string[]; current: number; strikes: number; state: string};

export default function Page() {
  const [journey, setJourney] = useState<Journey>();
  const [wallet, setWallet] = useState('');
  const [passage, setPassage] = useState('');
  const [message, setMessage] = useState('');
  const [chartOpen, setChartOpen] = useState(false);
  const [id, setId] = useState('');
  const [need, setNeed] = useState('');
  const [rules, setRules] = useState('');
  const [steps, setSteps] = useState('');

  const load = async () => {
    try {
      const page: any = await read('get_journeys_page', [0, 20]);
      setJourney((page.items || []).slice(-1)[0]);
    } catch {}
  };

  useEffect(() => { load(); }, []);

  const propose = async () => {
    try {
      setMessage('Wallet approval, then validator review. Keep this page open until FINALIZED.');
      const hash = await write('propose_passage', [journey!.id, passage]);
      setMessage(`FINALIZED: ${hash}`);
      setPassage('');
      await load();
    } catch (error: any) { setMessage(error.message); }
  };

  const create = async () => {
    try {
      setMessage('Wallet approval, then journey creation. Keep this page open until FINALIZED.');
      const hash = await write('chart_journey', [id, need, rules.split('\n').filter(Boolean), steps.split('\n').filter(Boolean)]);
      setMessage(`FINALIZED: ${hash}`);
      setChartOpen(false);
      await load();
    } catch (error: any) { setMessage(error.message); }
  };

  return <main>
    <header>
      <h1>ACCESS<br/><span>WEAVE</span></h1>
      <p>A shared route is only complete when every passage preserves the frozen access need.</p>
      <div className="headActions">
        <button className="quiet" onClick={() => setChartOpen(!chartOpen)}>{chartOpen ? 'CLOSE CHART' : 'CHART JOURNEY'}</button>
        <button onClick={async () => setWallet(await connect())}>{wallet ? wallet.slice(0, 6) + '...' + wallet.slice(-4) : 'CONNECT TRAVELER'}</button>
      </div>
    </header>
    {chartOpen && <section className="chart">
      <label>JOURNEY ID<input value={id} onChange={e => setId(e.target.value)}/></label>
      <label>ACCESS NEED<textarea value={need} onChange={e => setNeed(e.target.value)}/></label>
      <label>CONSTRAINTS, ONE PER LINE<textarea value={rules} onChange={e => setRules(e.target.value)}/></label>
      <label>ROUTE SEGMENTS, ONE PER LINE<textarea value={steps} onChange={e => setSteps(e.target.value)}/></label>
      <button disabled={id.length < 2 || need.length < 24 || rules.split('\n').filter(Boolean).length < 2 || steps.split('\n').filter(Boolean).length < 3} onClick={create}>PUNCH JOURNEY CARD</button>
    </section>}
    <section className="journey">
      <div className="need"><small>TRAVELER NEED</small><h2>{journey?.need || 'Waiting for a charted journey.'}</h2>{journey?.constraints.map(item => <span key={item}>{item}</span>)}</div>
      <div className="thread">{(journey?.segments || ['ORIGIN', 'TRANSFER', 'CROSSING', 'ARRIVAL']).map((item, index) => <article key={item} className={index <= (journey?.current || 0) ? 'lit' : ''}><i>{index + 1}</i><b>{item}</b><em>{index < (journey?.current || 0) ? 'CLEARED' : index === (journey?.current || 0) ? 'CURRENT' : 'SEALED'}</em></article>)}</div>
      <aside><strong>{journey?.strikes || 0}/3</strong><span>BARRIERS</span><p>{journey?.state || 'UNCHARTED'}</p></aside>
    </section>
    <section className="passage">
      <label>PROPOSE PASSAGE FOR {journey?.segments[journey?.current] || 'CURRENT SEGMENT'}</label>
      <textarea value={passage} onChange={e => setPassage(e.target.value)} placeholder="Describe the exact workaround and how it preserves every access constraint."/>
      <button disabled={!journey || passage.length < 24} onClick={propose}>TEST THIS PASSAGE</button>
    </section>
    {message && <div className="ticket">{message}</div>}
    <footer>STUDIONET / ACCESS-PRESERVING CONSENSUS</footer>
  </main>;
}
