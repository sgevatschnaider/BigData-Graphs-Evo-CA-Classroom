// WERC classroom numerical smoke tests, independent from browser DOM.
const assert=require("node:assert/strict");
const fs=require("node:fs");
const path=require("node:path");
const file=path.join(__dirname,"..","docs","assets","werc-2026","werc-labs.js");
const source=fs.readFileSync(file,"utf8");
const start=source.indexOf("function num(id)");
const end=source.indexOf("var info={");
assert(start>=0&&end>start,"Numerical core cannot be located");
const isolated=new Function(source.slice(start,end)+"return {softmax,graph,rho,solve};");
const {softmax,graph,rho,solve}=isolated();
function close(a,b,tol=1e-6){assert(Math.abs(a-b)<tol,"Expected "+a+" approximately "+b);}
const s=graph("STAR",4);
const p=graph("PATH",4);
close(rho(s),Math.sqrt(3));
close(rho(p),2*Math.cos(Math.PI/5));
const star=solve(s,.2);
const path4=solve(p,.2);
assert(star.stable&&path4.stable);
close(star.total,65/11);
close(path4.total,110/19);
close(star.x[0],20/11);
close(path4.x[1],30/19);
const q=softmax([80,80],.1);
const qNext=softmax([90,90],.1);
close(q[0],qNext[0]);close(q[1],qNext[1]);
close(softmax([90,80],.1)[0],1/(1+Math.exp(-1)));
const K=4,Z=star.total,mu=1-K/Z,restricted=star.x.map(v=>v*K/Z);
close(mu,21/65);close(restricted.reduce((a,b)=>a+b,0),4);
for(const family of ["ER","WS","BA","SBM"]){
  const W=graph(family,24,48,20261041);
  const edges=W.flat().reduce((a,b)=>a+b,0)/2;
  assert.equal(edges,48);
  assert.equal(W.length,24);
  assert(W.every((row,i)=>row.every((v,j)=>v===W[j][i])));
  assert(solve(W,.12).stable,family+" synthetic equilibrium should be stable in smoke test");
}
assert.equal(solve(s,.6).stable,false,"Star spectral failure must be detected");
console.log("WERC interactive math tests passed: softmax, spectral radius, exact equilibria, 4 synthetic families, shadow price.");
