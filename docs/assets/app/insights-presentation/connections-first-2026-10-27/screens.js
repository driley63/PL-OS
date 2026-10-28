(() => {
  const query = new URLSearchParams(location.search);
  const root = document.getElementById('plectara-refined-journey');
  const initialScene = query.get('scene') || 'insights';
  const themes = query.has('pair') ? ['light','dark'] : [query.get('theme') === 'dark' ? 'dark' : 'light'];
  if (query.get('scale') === '1') root.style.zoom = 1;
  if (query.has('pair')) document.body.classList.add('review-board');
  const E = (tag, cls, children, attrs={}) => {
    const el = document.createElement(tag); if(cls) el.className=cls;
    Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,v));
    (Array.isArray(children)?children:[children]).forEach(c=>{if(c!==null&&c!==undefined)el.append(c)}); return el;
  };
  const P=(text,cls='')=>E('p',cls,text);
  const S=(cls,text)=>E('span',cls,text);
  const I=name=>name==='stomach'?S('stomach-icon',''):E('i','',null,{'data-lucide':name,'aria-hidden':'true'});
  const codes={today:58986,today_outlined:62541,format_list_bulleted_outlined:61605,bar_chart_outlined:61116,question_answer_outlined:62173,insights:58183,insights_outlined:61746,settings_outlined:62318,more_horiz:58370,arrow_back:57490,emoji_events_outlined:61466,workspace_premium_outlined:984737,local_fire_department_outlined:61818,stars_outlined:62435,celebration_outlined:61240};
  const M=name=>E('span','material-icon',String.fromCodePoint(codes[name]),{'aria-hidden':'true'});
  const symbol=name=>S('symbol',I(name));
  const chevron=()=>E('i','chevron',null,{'data-lucide':'chevron-right','aria-hidden':'true'});
  const panel=(children,cls='')=>E('section','reading '+cls,children);
  const link=(children,action,cls='action full-link')=>{const b=E('button',cls+' link-button',children,{type:'button'});b.onclick=action;return b;};
  const patterns={
    digestion:{goal:'Better Digestion',icon:'stomach',status:'Possible Connection',state:'possible',mark:'link-2',signals:[['milk','Dairy-tagged meals'],['stomach','Bloating']],headline:'Bloating was logged near dairy-tagged meals.',context:'Seen in the past 14 days. Unlogged symptoms could affect this pattern.',detail:'Bloating was logged within four hours of some meals, before or after eating.'},
    energy:{goal:'More Energy',icon:'zap',status:'Possible Connection',state:'possible',mark:'link-2',signals:[['activity','Logged activity'],['zap','Energy ratings']],headline:'Energy ratings were higher on days with logged activity.',context:'Seen in recent rated days. Missing activity logs can affect the comparison.',detail:'A same-day association in your recorded check-ins. It does not show which came first.'}
  };
  const symptomGoal={goal:'Fewer, Milder Symptoms',icon:'heart-pulse'};
  const stateLabel=p=>E('div','pattern-state '+p.state,[I(p.mark),S('',p.status)]);
  const goalHeading=p=>E('div','row goal-heading',[symbol(p.icon),E('div','grow',[P(p.goal,'goal-name'),stateLabel(p)])]);
  const relationship=p=>E('div','relationship',[
    S('relation-end',[I(p.signals[0][0]),S('',p.signals[0][1])]),S('relation-line',''),I('link-2'),S('relation-line',''),S('relation-end',[I(p.signals[1][0]),S('',p.signals[1][1])])
  ],{role:'img','aria-label':p.signals[0][1]+' linked with '+p.signals[1][1]+'; no causal direction implied'});
  const sceneNames={insights:'Insights Overview',details:'Goal Details',today:'Today',energy:'Goal Details',gathering:'Gathering Context',plan:'Plan Management'};
  for(const theme of themes){
    const column=E('div',query.has('pair')?'review-column':'');
    if(query.has('pair')) column.append(P(sceneNames[initialScene]+' · '+(theme==='light'?'Light':'Dark'),'review-label'));
    const app=E('div','phone',null,{'data-theme':theme,'aria-label':'Plectara '+theme+' design study'});
    column.append(app);root.append(column);
    const yarn=E('div','yarn',E('img','',null,{src:'source/yarn.webp',alt:''}));
    const header=E('header','header'),main=E('main','main',null,{'aria-label':'Screen content'}),nav=E('nav','p-nav',null,{'aria-label':'Plectara tabs'}),capture=E('div','capture');
    app.append(yarn,header,main,capture,nav);
    let scene=initialScene==='gathering'?'insights':initialScene,filter=initialScene==='gathering'?'stress':'all';
    const go=s=>{scene=s;render()};
    const card=(key,today=false)=>{
      const p=key==='digestion'&&filter==='symptoms'?{...patterns[key],...symptomGoal}:patterns[key];const body=[];
      if(today)body.push(E('div','today-finding-label',[E('strong','','New Finding · Rule-Derived'),S('','On Your Device')]));
      body.push(goalHeading(p));if(p.signals)body.push(relationship(p));
      body.push(E('h3','pattern-headline',p.headline),P(p.context,'pattern-context'),S('summary-foot',[S('','Explore more about '+p.goal),chevron()]));
      return link(body,()=>go(key==='digestion'?'details':key),'reading connection-card');
    };
    const filters=()=>{
      const row=E('div','chip-row',null,{role:'group','aria-label':'Filter Insights by goal'});
      [['all','All Goals'],['symptoms','Fewer, Milder Symptoms'],['digestion','Better Digestion'],['energy','More Energy'],['stress','Less Stress']].forEach(([key,label])=>{const b=link((filter===key?'✓ ':'')+label,()=>{filter=key;render()},'chip');b.setAttribute('aria-pressed',filter===key);row.append(b)});
      return panel([E('div','filter-top',[P('Filter Insights','kicker'),P('Updated Today · 9:41 AM','meta')]),row,P('Rule-Derived · On Your Device','meta')],'filters');
    };
    const aiEntry=()=>link([E('div','row',[E('span','symbol ai',I('sparkles')),E('div','grow',[P('A Closer Look With AI','ai-title'),P('Review your eligible meal and symptom findings','meta')]),chevron()])],()=>go('ai-review'),'reading ai-entry');
    const rewards=()=>panel([E('div','row',[M('emoji_events_outlined'),E('h3','grow','Your Progress'),chevron()]),E('div','progress-tiles',[
      ['Badges','8','workspace_premium_outlined'],['Streak','90d','local_fire_department_outlined'],['Points','12.3K','stars_outlined']
    ].map(a=>E('div','progress-tile',[P(a[0],'progress-label'),E('div','progress-value',[M(a[2]),S('value',a[1])]),E('div','new-slot','')])) )],'rewards');
    const plan=(detail=false)=>panel([
      E('div','heading-row',[P("Today's Plan",'kicker'),P('Day 6 of 14','meta')]),P('Two-Week Meal and Symptom Check','plan-name'),P('Build a clearer record of meals and symptoms.','plan-subtitle'),
      E('div','row-status',[S('state-icon recorded',I('circle-check')),P('Meals','grow'),S('status-copy recorded','Recorded Today')]),
      E('div','row-status',[S('state-icon',I('circle')),P('Symptoms','grow'),S('status-copy meta','When Noticed')]),
      detail?P('Tracked automatically from your logs','evidence-note'):link([S('meta','Tracked from your logs'),S('inline-icon',[S('','View Plan'),chevron()])],()=>go('plan'),'plan-link')
    ],'plan-compact');
    const evidence=key=>{
      const energy=key==='energy';
      const rows=energy?[['Days With Logged Activity','7.2 / 10','7 days with energy ratings',72],['Days Without an Activity Log','5.1 / 10','6 days with energy ratings',51]]:[['Dairy-tagged Meals','3 of 8','38% with nearby logged bloating',37.5],['Meals Without a Dairy Tag','3 of 12','25% with nearby logged bloating',25]];
      const body=[E('h3','evidence-heading',energy?'Average Energy Ratings':'What the Records Show'),P(energy?'Oct 12–25 · Same-day energy ratings':'Oct 12–25 · Within four hours, before or after','meta')];
      rows.forEach(([label,value,coverage,width],i)=>{const fill=E('div','bar-fill');fill.style.width=width+'%';body.push(E('div','bar-row '+(i?'previous':'current'),[P(label,'bar-label'),E('div','bar-head',[P(coverage,'meta'),S('measure',value)]),E('div','bar-track',fill,{'aria-hidden':'true'})]))});
      body.push(P(energy?'Only days with an energy rating are compared. No activity log does not mean no activity.':'Counts include all tagged or untagged meals. No symptom log means unknown, not symptom-free.','evidence-note'));
      body.push(link([S('','Browse the Supporting Records'),chevron()],()=>go('records'),'record-link'));
      return panel(body,'evidence-card');
    };
    const gathering=()=>panel([E('div','row',[symbol('wind'),E('div','grow',[P('Less Stress','goal-name'),P('Still Gathering Context','meta')])]),P('Stress ratings alongside daily habits can help reveal possible connections. More records do not guarantee a finding.','pattern-context')],'connection-card');
    function render(){
      const isToday=scene==='today',isOverview=scene==='insights';
      app.classList.toggle('has-capture',isToday);header.replaceChildren();main.replaceChildren();capture.replaceChildren();
      header.append(E('div','status',[S('','9:41'),E('div','status-icons',[I('wifi'),I('battery-full')])]));
      const toolbar=E('div','toolbar');
      if(!isToday&&!isOverview){const back=link(M('arrow_back'),()=>go('insights'),'action icon-action');back.setAttribute('aria-label','Back to Insights');toolbar.append(back);}
      toolbar.append(isToday?E('div','brand',E('img','',null,{src:'source/logo.svg',alt:'Plectara'})):E('h2','',isOverview?'Insights':scene==='plan'?'Your Plan':scene==='records'?'Supporting Records':(scene==='details'&&filter==='symptoms'?symptomGoal.goal:patterns[scene==='details'?'digestion':scene]?.goal||'Insights')));
      if(!isToday)toolbar.append(E('button','action icon-action',M('more_horiz'),{'aria-label':'Insights options',type:'button'}));
      if(isToday||isOverview)toolbar.append(E('button','action icon-action',M('settings_outlined'),{'aria-label':'Settings',type:'button'}));header.append(toolbar);
      if(isOverview){
        main.append(filters());Object.keys(patterns).filter(k=>filter==='all'||filter===k||(filter==='symptoms'&&k==='digestion')).forEach(k=>main.append(card(k)));
        if(filter==='all'||filter==='stress')main.append(gathering());
        if(['all','digestion','symptoms'].includes(filter))main.append(aiEntry());
        if(filter==='stress')main.append(panel([E('h3','','Keep Building Context'),P('Record a stress rating in your daily check-in. Log the habits you want to understand alongside it.','pattern-context'),P('Your check-in findings stay on your device.','evidence-note')],'connection-card'));
        main.append(plan());
      }else if(isToday){
        main.append(plan(),card('energy',true),rewards(),panel([link([S('','See All Insights'),chevron()],()=>go('insights'))]));
        capture.append(E('button','action quick',[I('zap'),'Quick Log'],{type:'button'}),E('button','action log',[I('plus'),'Log'],{type:'button'}));
      }else if(['details','energy'].includes(scene)){
        const key=scene==='details'?'digestion':'energy',p=key==='digestion'&&filter==='symptoms'?{...patterns[key],...symptomGoal}:patterns[key];
        main.append(panel([P('Rule-Derived · On Your Device','source-note'),goalHeading(p),relationship(p),E('h3','pattern-headline',p.headline),P(p.detail,'pattern-context')],'connection-card details-card'),evidence(key),panel([
          E('h3','','How to Read This Pattern'),P(key==='digestion'?'Meal size, other ingredients, and timing may also matter. This finding also relates to Fewer, Milder Symptoms.':'Sleep, other routines, and which days you log may affect this comparison. This finding stays on your device.','pattern-context'),P('This is an association, not proof of a cause.','evidence-note'),
          ...(key==='digestion'?[link([I('messages-square'),S('grow','Ask About This Pattern'),chevron()],()=>go('chat'),'action full-link')]:[])
        ],'connection-card'));
        if(key==='digestion')main.append(panel([P('Your Active Plan','kicker'),E('h3','','Two-Week Meal and Symptom Check'),P('Record meals near eating and symptoms when noticed. This plan follows your meal and symptom records.','pattern-context'),link([S('','View Plan'),chevron()],()=>go('plan'))],'connection-card'));
      }else if(scene==='gathering'){
        filter='stress'; main.append(filters(),gathering(),panel([E('h3','','Keep Building Context'),P('Record a stress rating in your daily check-in. Log the habits you want to understand alongside it.','pattern-context'),P('Your check-in findings stay on your device.','evidence-note')],'connection-card'));
      }else if(scene==='plan'){
        main.append(plan(true),panel([E('h3','','What This Plan Follows'),P('Meals and symptoms over two weeks. Add meal details near eating, and record symptoms with severity when you notice them.','pattern-context'),P('A missing symptom log does not count as a symptom-free day.','evidence-note')],'connection-card'),panel([E('h3','','Manage This Plan'),P('Pause tracking or end the plan. Your logs remain available.','pattern-context'),link([I('pause'),S('','Pause Plan')],()=>go('paused'),'manage-button'),link([I('square'),S('','End Plan')],()=>go('end'),'manage-button end-button')],'connection-card'));
      }else if(scene==='paused'){
        main.append(panel([E('h3','','Plan Paused'),P('Two-Week Meal and Symptom Check','pattern-context'),link([I('play'),S('','Resume Plan')],()=>go('plan'),'manage-button')],'connection-card'));
      }else if(scene==='end'){
        main.append(panel([E('h3','','End This Plan?'),P("Stop this plan’s tracking? Your logs remain available.",'pattern-context'),link('Keep the Plan',()=>go('plan'),'manage-button'),link('End Plan',()=>go('ended'),'manage-button end-button')],'connection-card'));
      }else if(scene==='ended'){
        main.append(panel([E('h3','','The Plan Ended Early'),P('Your entries remain available. Ending tracking is not an assessment.','pattern-context')],'connection-card'));
      }else if(scene==='records'){
        main.append(panel([E('h3','','Records Behind This Finding'),P('The production view opens the exact evidence records using structured references or a reproducible selection.','pattern-context'),P('This design reference does not contain individual diary entries.','evidence-note')],'connection-card'));
      }else if(scene==='ai-review'){
        main.append(panel([P('AI-Assisted · Eligible Findings','kicker'),E('h3','','A Closer Look With AI'),P('This reference shows the entry point. The full review uses only eligible shared findings, with its own timestamp and context disclosure.','pattern-context'),P('Energy, mood, stress and cycle findings remain on your device.','evidence-note')],'connection-card'));
      }else if(scene==='chat'){
        main.append(panel([P('AI-Assisted · Finding Context','kicker'),E('h3','','Ask About This Pattern'),P('What else could help explain the connection?','pattern-context')],'connection-card'));
      }
      capture.hidden=!isToday;
      if(query.has('lower')&&isOverview)requestAnimationFrame(()=>{main.scrollTop=main.scrollHeight-main.clientHeight});
      const tabs=E('div','destinations');
      [['today','today','Today'],['timeline','format_list_bulleted','Timeline'],['charts','bar_chart','Charts'],['chat','question_answer','Chat'],['insights','insights','Insights']].forEach(([key,icon,label])=>{
        const active=key===(isToday?'today':scene==='chat'?'chat':'insights');
        const glyph=active&&codes[icon]?icon:icon+'_outlined';
        const b=link([S('nav-icon',M(glyph)),S('',label)],()=>{if(['today','insights','chat'].includes(key))go(key)},'nav-button');
        if(active)b.setAttribute('aria-current','page');tabs.append(b);
      });nav.replaceChildren(tabs,E('div','home-indicator'));main.scrollTop=0;
      if(window.lucide)lucide.createIcons({attrs:{width:20,height:20}});
      requestAnimationFrame(()=>{const row=main.querySelector('.chip-row'),selected=row?.querySelector('[aria-pressed="true"]');if(row&&selected){const a=row.getBoundingClientRect(),b=selected.getBoundingClientRect(),scale=app.getBoundingClientRect().width/app.offsetWidth;if(b.right>a.right)row.scrollLeft+=(b.right-a.right)/scale;if(b.left<a.left)row.scrollLeft-=(a.left-b.left)/scale;}});
    }
    render();
    const c=Math.cos(55*Math.PI/180),s=Math.sin(55*Math.PI/180);
    app.style.setProperty('--yw',(393*c+852*s+32)+'px');app.style.setProperty('--yh',(393*s+852*c+32)+'px');
  }
  document.title=(sceneNames[initialScene]||'Plectara')+' · Connections First · Illustrative Design';
  Promise.all([document.fonts.ready,...Array.from(document.images).map(i=>i.decode().catch(()=>{}))]).then(()=>requestAnimationFrame(()=>requestAnimationFrame(()=>document.documentElement.dataset.captureReady='true')));
})();
