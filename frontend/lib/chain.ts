'use client';

import {createAccount, createClient} from 'genlayer-js';
import {studionet} from 'genlayer-js/chains';

export const A = (process.env.NEXT_PUBLIC_CONTRACT_ADDRESS ||
  '0x5563fC521Bc7dA579F9899bb03ED0d3b2bB1C408') as `0x${string}`;

const endpoint = 'https://studio.genlayer.com/api';
const reader: any = createClient({chain: studionet, endpoint, account: createAccount()});
let writer: any;

export async function connect() {
  const provider: any = (window as any).ethereum;
  if (!provider) throw Error('Browser wallet required');
  const [address] = await provider.request({method: 'eth_requestAccounts'});
  writer = createClient({chain: studionet, endpoint, account: address, provider});
  return address;
}

export const read = (name: string, args: any[] = []) =>
  reader.readContract({address: A, functionName: name, args});

export async function write(name: string, args: any[] = []) {
  if (!writer) throw Error('Connect wallet');
  const hash = await writer.writeContract({address: A, functionName: name, args, value: 0n});
  await writer.waitForTransactionReceipt({
    hash,
    status: 'FINALIZED',
    retries: 180,
    interval: 5000,
  });
  return hash as string;
}
