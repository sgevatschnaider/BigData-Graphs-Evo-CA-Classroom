(function(){
"use strict";
var $=function(id){return document.getElementById(id)},stage=$("lab-stage"),current=1;
function num(id){return Number($(id).value)}
function f(x,n){return Number.isFinite(x)?Number(x).toFixed(n===undefined?3:n):"—"}
function softmax(q,beta){var x=q.map(function(v){return beta*v}),m=Math.max.apply(null,x),e=x.map(function(v){return Math.exp(v-m)}),d=e.reduce(function(a,b){return a+b},0);return e.map(function(v){return v/d})}
function zero(n){return Array.from({length:n},function(){return Array(n).fill(0)})}
function link(a,i,j){if(i!==j){a[i][j]=1;a[j][i]=1}}
function rand(seed){var s=seed>>>0;return function(){s+=0x6D2B79F5;var t=s;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return ((t^t>>>14)>>>0)/4294967296}}
function graph(type,n,m,seed){var a=zero(n),r=rand(seed||20261020),edges=[],i,j,k;
if(type==="STAR"){for(i=1;i<n;i++)link(a,0,i);return a}
if(type==="PATH"){for(i=1;i<n;i++)link(a,i-1,i);return a}
if(type==="WS"){for(i=0;i<n;i++)for(j=1;j<=2;j++)link(a,i,(i+j)%n);
for(i=0;i<n;i++)for(j=1;j<=2;j++){k=(i+j)%n;if(a[i][k]&&r()<.12){var cand=[];for(var z=0;z<n;z++)if(z!==i&&!a[i][z])cand.push(z);if(cand.length){a[i][k]=a[k][i]=0;link(a,i,cand[Math.floor(r()*cand.length)])}}}}
else if(type==="BA"){link(a,0,1);link(a,1,2);link(a,0,2);for(i=3;i<n;i++)for(k=0;k<2;k++){var weights=[],sum=0;for(j=0;j<i;j++){var d=a[j].reduce(function(s,v){return s+v},0)+.00001;if(a[i][j])d=0;weights.push(d);sum+=d}var pick=r()*sum,chosen=i-1;for(j=0;j<i;j++){pick-=weights[j];if(pick<=0){chosen=j;break}}link(a,i,chosen)}}
else if(type==="SBM"){for(i=0;i<n;i++)for(j=i+1;j<n;j++)if(r()<((i<n/2)===(j<n/2)?.31:.018))link(a,i,j)}
else if(type==="ER"){var pairs=[];for(i=0;i<n;i++)for(j=i+1;j<n;j++)pairs.push([i,j]);for(k=0;k<m;k++){j=k+Math.floor(r()*(pairs.length-k));var temp=pairs[j];pairs[j]=pairs[k];pairs[k]=temp;link(a,pairs[k][0],pairs[k][1])}}
if(type!=="ER"){var have=[],missing=[];for(i=0;i<n;i++)for(j=i+1;j<n;j++)(a[i][j]?have:missing).push([i,j]);
while(have.length>m){var d1=Math.floor(r()*have.length),e1=have.splice(d1,1)[0];a[e1[0]][e1[1]]=a[e1[1]][e1[0]]=0}
while(have.length<m&&missing.length){var d2=Math.floor(r()*missing.length),e2=missing.splice(d2,1)[0];link(a,e2[0],e2[1]);have.push(e2)}}return a}
function rho(a){var n=a.length,x=Array(n).fill(1/Math.sqrt(n)),e=0,shift=1+Math.max.apply(null,a.map(function(row){return row.reduce(function(s,v){return s+v},0)}));for(var k=0;k<360;k++){var y=a.map(function(row,i){return shift*x[i]+row.reduce(function(s,v,j){return s+v*x[j]},0)}),norm=Math.hypot.apply(null,y);if(norm<1e-12)return 0;x=y.map(function(v){return v/norm});var z=a.map(function(row){return row.reduce(function(s,v,j){return s+v*x[j]},0)});e=x.reduce(function(s,v,j){return s+v*z[j]},0)}return e}
function solve(a,eta){var n=a.length,rr=rho(a),stable=eta*rr<1-1e-9;if(!stable)return {stable:false,rho:rr,x:[],total:NaN};var x=Array(n).fill(1);
for(var k=0;k<2800;k++){var y=a.map(function(row){return 1+eta*row.reduce(function(s,v,j){return s+v*x[j]},0)}),delta=Math.max.apply(null,y.map(function(v,j){return Math.abs(v-x[j])}));x=y;if(delta<1e-10)break}
return {stable:true,rho:rr,x:x,total:x.reduce(function(s,v){return s+v},0)}}
function points(n,type){if(type==="STAR"){var p=[[300,200]];for(var i=1;i<n;i++){var a=2*Math.PI*(i-1)/(n-1)-Math.PI/2;p.push([300+155*Math.cos(a),200+150*Math.sin(a)])}return p}
if(type==="PATH")return Array.from({length:n},function(_,i){return [55+i*490/(n-1),200]});
return Array.from({length:n},function(_,i){var a=2*Math.PI*i/n-Math.PI/2;return[300+170*Math.cos(a),200+165*Math.sin(a)]})}
function network(a,values,type){var p=points(a.length,type),s='<svg class="chartsvg" viewBox="0 0 600 410" role="img" aria-label="Red sintética modificable con '+a.length+' nodos">',max=values?Math.max.apply(null,values):1,min=values?Math.min.apply(null,values):0;
for(var i=0;i<a.length;i++)for(var j=i+1;j<a.length;j++)if(a[i][j])s+='<line x1="'+p[i][0]+'" y1="'+p[i][1]+'" x2="'+p[j][0]+'" y2="'+p[j][1]+'" stroke="#5bc5dc" stroke-opacity=".45" stroke-width="2"/>';
for(i=0;i<a.length;i++){var t=values?(values[i]-min)/(max-min||1):.3,rad=a.length<=8?22:8+11*t;s+='<circle cx="'+p[i][0]+'" cy="'+p[i][1]+'" r="'+rad+'" fill="hsl('+(182-145*t)+' 84% 60%)" stroke="#c8fffa" stroke-width="1.2"/>';if(a.length<=8)s+='<text x="'+p[i][0]+'" y="'+(p[i][1]+4)+'" font-size="11" text-anchor="middle" font-weight="bold" fill="#032736">'+(i+1)+'</text>'}
return s+'</svg>'}
function bars(labels,values){var ymax=Math.max.apply(null,values.concat([1]))*1.16,s='<svg class="chartsvg" viewBox="0 0 600 260" role="img" aria-label="Barras comparativas">';
for(var k=0;k<5;k++){var y=23+k*48;s+='<line x1="45" y1="'+y+'" x2="575" y2="'+y+'" stroke="#6f92a7" opacity=".24"/>'}
for(var i=0;i<labels.length;i++){var step=520/labels.length,x=50+i*step+step*.18,h=values[i]/ymax*184,y0=214-h;s+='<rect x="'+x+'" y="'+y0+'" width="'+(step*.65)+'" height="'+h+'" rx="7" fill="'+["#70eee2","#ffca87","#aca3ef","#fe9aaa"][i%4]+'"/><text x="'+(x+step*.33)+'" y="'+(y0-6)+'" fill="#e5ffff" font-size="12" text-anchor="middle">'+f(values[i],2)+'</text><text x="'+(x+step*.33)+'" y="237" fill="#b5cee0" font-size="12" text-anchor="middle">'+labels[i]+'</text>'}
return s+'</svg>'}
function metrics(a){return'<div class="kpis">'+a.map(function(v){return'<div class="kpi"><span class="val">'+v[1]+'</span><span class="key">'+v[0]+'</span></div>'}).join("")+'</div>'}
function range(id,label,min,max,step,value){return'<div class="lab-control"><label for="'+id+'">'+label+' <output id="'+id+'-value">'+value+'</output></label><input id="'+id+'" type="range" min="'+min+'" max="'+max+'" step="'+step+'" value="'+value+'"></div>'}
function select(id,label,opts){return'<div class="lab-control"><label for="'+id+'">'+label+'</label><select id="'+id+'">'+opts.map(function(o){return'<option value="'+o[0]+'">'+o[1]+'</option>'}).join("")+'</select></div>'}
function shell(inputs,warning){stage.innerHTML='<div class="lab-columns"><div class="params"><h4>Parámetros</h4>'+inputs+'</div><div class="viz"><h4>Modelo en vivo</h4><div id="plot"></div><div id="stat"></div></div></div><div class="lab-note">'+warning+'</div>'}
function listen(ids,fn){ids.forEach(function(id){$(id).addEventListener("input",fn);$(id).addEventListener("change",fn)});fn()}
function values(ids){ids.forEach(function(id){var v=$(id);if($(id+"-value"))$(id+"-value").textContent=f(Number(v.value),Number(v.step)<.1?2:1)})}
function lab1(){shell(select("scenario","Tipo de mejora",[["all","Ambos laboratorios"],["first","Solo laboratorio A"]])+range("q","Capacidad inicial",50,100,1,80)+range("g","Mejora",0,30,1,10)+range("beta","Sensibilidad β",.02,.25,.01,.1),"El desplazamiento común deja invariante la cuota: σᵢ(q+g𝟙)=σᵢ(q). No demuestra sobreinversión.");
function draw(){values(["q","g","beta"]);var q=num("q"),g=num("g"),b=num("beta"),p=softmax([q,q],b),after=softmax($("scenario").value==="all"?[q+g,q+g]:[q+g,q],b);
$("plot").innerHTML=bars(["A antes","B antes","A luego","B luego"],p.concat(after).map(function(v){return v*100}));
$("stat").innerHTML=metrics([["Cuota A inicial",f(p[0]*100,1)+"%"],["Cuota A final",f(after[0]*100,1)+"%"],["Cambio A",f(100*(after[0]-p[0]),2)+" pp"],["Suma final",f(100*(after[0]+after[1]),1)+"%"]])+'<pre class="math">σᵢ=exp(βqᵢ)/Σ exp(βqⱼ)</pre>'}listen(["scenario","q","g","beta"],draw)}
function lab2(){shell(select("shape","Forma de red",[["STAR","Estrella K₁,₃"],["PATH","Camino P₄"]])+range("focus","Nodo que inspeccionás",1,4,1,1),"Wᶜ es una red de influencia competitiva conceptual; las conexiones no son contratos observados.");
function draw(){values(["focus"]);var type=$("shape").value,a=graph(type,4),i=num("focus")-1;var ns=a[i].flatMap(function(v,j){return v?[j+1]:[]});
$("plot").innerHTML=network(a,null,type);
$("stat").innerHTML=metrics([["Nodos","4"],["Enlaces","3"],["Grado del nodo",ns.length],["Radio espectral",f(rho(a),4)]])+'<pre class="math">Vecinos de '+(i+1)+': '+ns.join(", ")+'\nWᶜ =\n'+a.map(function(row){return "["+row.join(" ")+"]"}).join("\n")+'</pre>'}listen(["shape","focus"],draw)}
function lab3(){shell(select("shape","Topología",[["STAR","Estrella K₁,₃"],["PATH","Camino P₄"]])+range("eta","Interacción η=α/b",0,.65,.01,.2),"La condición ρ(ηW)<1 garantiza equilibrio interior bajo los demás supuestos. No graficamos resultados fuera del dominio garantizado.");
function draw(){values(["eta"]);var type=$("shape").value,a=graph(type,4),eta=num("eta"),r=solve(a,eta);$("plot").innerHTML=network(a,r.stable?r.x:null,type);
$("stat").innerHTML=metrics([["ρ(W)",f(r.rho,4)],["ηρ(W)",f(eta*r.rho,4)],["Σ inversión",r.stable?f(r.total,4):"Fuera de rango"],["Condición",r.stable?"Cumple":"No cumple"]])+(r.stable?bars(["L1","L2","L3","L4"],r.x):'<p class="lab-bad">No hay garantía de equilibrio interior.</p>')+'<pre class="math">x*=(I−ηW)⁻¹𝟙\n'+(r.stable?r.x.map(function(v){return f(v,4)}).join(" ; "):"La resolvente no converge en el rango especificado")+'</pre>'}listen(["shape","eta"],draw)}
function lab4(){shell(select("family","Familia",[["ER","Aleatoria ER"],["WS","Mundo pequeño WS"],["BA","Escala libre BA"],["SBM","Modular SBM"]])+range("seed","Semilla adicional",0,100,1,21)+range("eta","Interacción η",.02,.15,.005,.12),"La tabla muestra promedios REPORTADOS de 480 grafos del artículo. Este generador es nuevo y no reproduce el CSV ni el código original del estudio.");
var reported={ER:[4.817,50.998,1.553,.275],WS:[4.148,46.743,.242,.210],BA:[5.214,55.692,3.372,.335],SBM:[4.815,50.214,1.504,.264]};
function draw(){values(["seed","eta"]);var type=$("family").value,a=graph(type,24,48,20261020+num("seed")),r=solve(a,num("eta"));$("plot").innerHTML=network(a,r.stable?r.x:null,type);
$("stat").innerHTML=metrics([["Nodos","24"],["Aristas","48"],["ρ actual",f(r.rho,3)],["Σ inversión actual",r.stable?f(r.total,3):"No estable"]])+'<p style="font-size:.76rem;color:#aed5dc">Medias reportadas del experimento WERC, 120 por familia:</p><table class="data-table"><thead><tr><th>Red</th><th>ρ media</th><th>Σx ± DE</th><th>μ</th></tr></thead><tbody>'+Object.keys(reported).map(function(k){var v=reported[k];return'<tr'+(k===type?' style="background:#174057"':'')+'><td>'+k+'</td><td>'+f(v[0])+'</td><td>'+f(v[1])+' ± '+f(v[2])+'</td><td>'+f(v[3])+'</td></tr>'}).join("")+'</tbody></table>'}listen(["family","seed","eta"],draw)}
function lab5(){shell(select("shape","Topología",[["STAR","Estrella"],["PATH","Camino"]])+range("capacity","Capacidad K",1,8,.1,4)+range("eta","Intensidad η",0,.4,.01,.2),"Una única capacidad homogénea vinculante fija Σx*=K. La red cambia la distribución y μ. No generalizar a recursos múltiples.");
function draw(){values(["capacity","eta"]);var type=$("shape").value,a=graph(type,4),K=num("capacity"),r=solve(a,num("eta")),bind=r.stable&&K<r.total,mu=bind?1-K/r.total:0,x=r.stable?(bind?r.x.map(function(v){return v*K/r.total}):r.x):[];
$("plot").innerHTML=network(a,r.stable?x:null,type);
$("stat").innerHTML=metrics([["Demanda Z",f(r.total)],["Capacidad K",f(K,2)],["Precio sombra μ",f(mu,4)],["Inversión Σx*",f(x.reduce(function(a,b){return a+b},0))]])+(r.stable?bars(["L1","L2","L3","L4"],x):"")+'<pre class="math">'+(bind?"x*=(K/Z)z\nμ=1−K/Z\nΣx*=K":r.stable?"K no es vinculante\nμ=0, x*=z":"Condición espectral incumplida")+'</pre>'}listen(["shape","capacity","eta"],draw)}
function lab6(){shell(range("G","Ganancia por desvío G",.1,2,.05,.8)+range("d","Detección d",0,1,.05,.5)+range("sanction","Sanción Pₛ",0,2,.05,.25)+range("delta","Paciencia δ",.1,.95,.01,.7)+range("future","Pérdida futura ΔU",.1,2,.05,.6),"La probabilidad estatal de detección no está derivada de la capa H. La sanción y el castigo futuro creíble son supuestos del juego.");
function draw(){values(["G","d","sanction","delta","future"]);var G=num("G"),d=num("d"),p=num("sanction"),delta=num("delta"),L=num("future"),rhs=d*p+delta*d/(1-delta)*L,margin=rhs-G,remaining=G-d*p,critical=remaining<=0?0:d>0?remaining/(remaining+d*L):Infinity;
$("plot").innerHTML=bars(["Desviación","Disuasión"],[G,rhs]);
$("stat").innerHTML=metrics([["G",f(G)],["Disuasión",f(rhs)],["δ mínimo",f(critical)],["Resultado",margin>=0?"Cumple*":"No cumple"]])+'<pre class="math">G ≤ d·Pₛ + [δd/(1−δ)]·ΔU\nMargen = '+f(margin,4)+'</pre>'}listen(["G","d","sanction","delta","future"],draw)}
function lab7(){shell(select("layer","Relación",[["W","W: Rivalidad"],["B","B: Infraestructura"],["H","H: Supervisión"],["F","F: Financiación (agenda)"]])+range("number","Aristas ilustrativas",1,8,1,5),"Los actores IA-A, IA-B, IA-C y IA-D son ficticios. Esta visualización no demuestra relaciones comerciales, exposición financiera ni causalidad.");
function draw(){values(["number"]);var layer=$("layer").value,count=num("number"),labs=["IA-A","IA-B","IA-C","IA-D"],others=layer==="B"?["Chips","Nube","Energía","Centros"]:layer==="H"?["Regulador","Auditor","Norma","Supervisor"]:layer==="F"?["Banca","Capital","Mercado","Inversor"]:["IA-A","IA-B","IA-C","IA-D"],edges=layer==="W"?[[0,1],[0,2],[1,3],[2,3],[0,3],[1,2]]:[[0,0],[0,1],[1,1],[1,2],[2,2],[2,3],[3,3],[3,0]],s='<svg class="chartsvg" viewBox="0 0 600 370" role="img" aria-label="Relaciones sintéticas entre categorías de actores">';
edges.slice(0,count).forEach(function(e){s+='<line x1="160" y1="'+(56+e[0]*78)+'" x2="440" y2="'+(56+e[1]*78)+'" stroke="#5eeadc" stroke-width="2.6"/>'});
for(var i=0;i<4;i++){s+='<rect x="58" y="'+(36+i*78)+'" rx="11" width="100" height="41" fill="#206f8e" stroke="#85e5ea"/><text x="108" y="'+(62+i*78)+'" fill="white" font-size="13" text-anchor="middle">'+labs[i]+'</text><rect x="442" y="'+(36+i*78)+'" rx="11" width="116" height="41" fill="#947348" stroke="#ffd58d"/><text x="500" y="'+(62+i*78)+'" fill="white" font-size="13" text-anchor="middle">'+others[i]+'</text>'}s+='</svg>';
$("plot").innerHTML=s;$("stat").innerHTML=metrics([["Capa",layer],["Actores ficticios","4"],["Enlaces simulados",String(Math.min(count,edges.length))],["Inferencia causal","Ninguna"]])+'<pre class="math">Wᶜ: n×n\nB: n×m\nH: r×n\nF: requiere definición operacional</pre>'}listen(["layer","number"],draw)}
function lab8(){shell(select("mode","Criterio de evaluación",[["fixed","Fijo"],["evolving","Coevolutivo (simplificado)"]])+range("epochs","Épocas",2,10,1,6)+range("gain","Incremento de calidad",.02,.16,.01,.08)+range("demand","Incremento de exigencia",.01,.12,.01,.05),"Modelo didáctico diferente del algoritmo RQGM. En el paper, el reemplazo exige mejorar frente a un ancla independiente; los scores dependientes se invalidan y los criterios permanecen fijos en cada época. NO replica sus garantías.");
function draw(){values(["epochs","gain","demand"]);var n=num("epochs"),gain=num("gain"),demand=num("demand"),evolving=$("mode").value==="evolving",q=.3,e=.28,rows=[];
for(var i=1;i<=n;i++){q=q+gain*(1-q);if(evolving&&i>1)e+=demand;rows.push({i:i,q:q,e:e,score:Math.max(0,Math.min(100,100*(q-e+.35)))})}
var plot='<svg class="chartsvg" viewBox="0 0 600 290" role="img" aria-label="Progreso sintético por épocas"><text x="28" y="25" font-size="14" fill="#c4dce6">Puntuación pedagógica</text><line x1="45" y1="240" x2="568" y2="240" stroke="#7394aa"/><polyline fill="none" stroke="#6ee8d9" stroke-width="4" points="'+rows.map(function(v,j){return (65+j*480/(n-1))+","+(236-v.score*1.65)}).join(" ")+'"/>';
rows.forEach(function(v,j){plot+='<circle cx="'+(65+j*480/(n-1))+'" cy="'+(236-v.score*1.65)+'" r="6.5" fill="#ffca8a"/><text x="'+(65+j*480/(n-1))+'" y="266" text-anchor="middle" fill="#c9dbe8" font-size="12">'+v.i+'</text>'});plot+='</svg>';
var last=rows[rows.length-1];$("plot").innerHTML=plot;$("stat").innerHTML=metrics([["Épocas",n],["Calidad artificial",f(last.q)],["Exigencia artificial",f(last.e)],["Reemplazos hipotéticos",evolving?n-1:0]])+'<table class="data-table"><thead><tr><th>Época</th><th>Agente</th><th>Evaluador</th><th>Puntaje*</th></tr></thead><tbody>'+rows.map(function(v){return'<tr><td>'+v.i+'</td><td>'+f(v.q)+'</td><td>'+f(v.e)+'</td><td>'+f(v.score,1)+'</td></tr>'}).join("")+'</tbody></table><p style="font-size:.74rem;color:#b9cbd8">*Puntaje artificial para ilustrar un criterio móvil; no es una métrica publicada del artículo RQGM.</p>'}listen(["mode","epochs","gain","demand"],draw)}
var info={
1:["La paradoja de la Reina Roja","RESULTADO I · CAPACIDAD RELATIVA","Si ambos laboratorios progresan exactamente lo mismo, sus cuotas softmax permanecen invariantes.",lab1],
2:["La red competitiva Wᶜ","REDES · ADYACENCIA","Dos redes de cuatro nodos y tres enlaces pueden tener distinta organización y radio espectral.",lab2],
3:["Equilibrio de Nash y espectro","RESULTADO II · EQUILIBRIO","Mové η y examiná el dominio espectral de un equilibrio interior y su distribución nodal.",lab3],
4:["Cuatro familias de grafos","EXPERIMENTACIÓN · TOPOLOGÍA","Una nueva red didáctica de 24 nodos se contrasta visualmente con las estadísticas reportadas de WERC.",lab4],
5:["Infraestructura y precio sombra","RESULTADO III · ESCASEZ","Bajo capacidad homogénea vinculante cambia el reparto de inversión y μ, no el total K.",lab5],
6:["Coordinación verificable","RESULTADO IV · JUEGO REPETIDO","Cambiá sanción, monitoreo y paciencia para comprobar una condición reducida de no desviación.",lab6],
7:["Cuatro capas: de laboratorios a mercados","EXTENSIÓN · HIPÓTESIS","Explorá por separado los tipos de relación W, B, H y la futura F financiera.",lab7],
8:["Red Queen Gödel Machine","FRONTERA · COEVOLUCIÓN","Compará evaluadores fijos y dinámicos en un ejemplo deliberadamente simplificado.",lab8]
};
function show(n,hash){current=Math.max(1,Math.min(8,Number(n)||1));var item=info[current];$("lab-kicker").textContent=item[1]+" · "+String(current).padStart(2,"0")+"/08";$("lab-title").textContent=item[0];$("lab-desc").textContent=item[2];
document.querySelectorAll("#lab-nav button").forEach(function(b){var ok=Number(b.dataset.lab)===current;b.classList.toggle("active",ok);b.setAttribute("aria-current",ok?"true":"false")});
try{item[3]()}catch(error){console.error(error);stage.innerHTML='<p class="lab-note lab-bad">No se pudo calcular este laboratorio. Revisá parámetros o JavaScript.</p>'}
if(hash)history.replaceState(null,"","#lab-"+String(current).padStart(2,"0"))}
$("lab-nav").addEventListener("click",function(evt){var b=evt.target.closest("button[data-lab]");if(b){show(b.dataset.lab,true);$("laboratorios").scrollIntoView({behavior:"smooth"})}});
document.querySelectorAll("[data-openlab]").forEach(function(a){a.addEventListener("click",function(){show(a.dataset.openlab,true)})});
window.addEventListener("hashchange",function(){var m=location.hash.match(/^#lab-0?([1-8])$/);if(m)show(m[1],false)});
var m=location.hash.match(/^#lab-0?([1-8])$/);show(m?m[1]:1,false);
window.WERC={softmax:softmax,graph:graph,rho:rho,solve:solve};
})();