(()=>{
const root=document.getElementById('plectara-preferences-study');
const config={descriptions:true,textScale:1,beverages:true,bowel:true,cycle:false};
const sections={
 profile:{title:'Health Profile',icon:'contact-round',summary:'Goals, personal details, and medications',intro:'The health context that helps Plectara understand your records.',groups:[['Your Direction',['goals']],['About You',['about','conditions','medications']]]},
 tracking:{title:'Tracking & Routines',icon:'list-checks',summary:'Log types, symptoms, and daily routines',intro:'Choose what you record and make everyday logging work for you.',groups:[['What You Record',['track','symptoms']],['Logging Preferences',['beverages','activity','sleep','daily','cycle']]]},
 quick:{title:'Quick Log & Widgets',icon:'panels-top-left',summary:'Saved items, widget pins, and habits',intro:'Set up reusable entries and the shortcuts you use to log them.',groups:[['Saved Items',['meals','saved-activities','bowel']],['Shortcuts & Habits',['capture']]]},
 ai:{title:'AI Insights & Chat',icon:'sparkles',summary:'Optional AI and what you share',intro:'Plectara finds patterns on this device. Optional cloud AI explains findings and helps you ask follow-up questions.'},
 reminders:{title:'Reminders',icon:'bell',summary:'Sleep, medications, and check-ins',intro:'Review your reminders in one place. Their times follow the same settings used in Sleep, Medications, and Check-Ins.'},
 appearance:{title:'Appearance',icon:'sun-moon',summary:'Light, dark, or your device setting'},
 progress:{title:'Your Progress',icon:'trophy',summary:'Points, streaks, and badges'},
 connections:{title:'Health Connections',icon:'heart-pulse',summary:'Apple Health or Health Connect'},
 account:{title:'Account & Privacy',icon:'shield-user',summary:'Sign-in, data export, and policies',intro:'Manage your account and the information you choose to share.',groups:[['Your Account',['identity','security']],['Your Information',['export','privacy','terms']]]}
};
const items={
 goals:{title:'Your Goals',icon:'flag',summary:'Choose the outcomes that matter to you',group:'profile',body:'Choose from Plectara’s existing health goals. Symptoms remain part of your insights whether or not you select a goal.'},
 about:{title:'About You',icon:'contact-round',summary:'Birthday, sex assigned at birth, and weight',group:'profile',body:'Review the personal details used to tailor your tracking experience.'},
 conditions:{title:'Conditions',icon:'heart-pulse',summary:'Your diagnosed current conditions',group:'profile',body:'Manage the diagnosed conditions you want Plectara to consider alongside your records.'},
 medications:{title:'Medications',icon:'pill',summary:'Medications, supplements, and schedules',group:'profile',body:'Manage your medications and supplements, including their logging schedules and reminders.'},
 track:{title:'What to Track',icon:'list-checks',summary:'Choose which logs are available',group:'tracking',body:'Symptoms stay on. Turning another log off keeps existing entries and stops new imports for that log. Turning it back on includes imports again from the day you started the app.'},
 symptoms:{title:'Symptoms',icon:'activity',summary:'Symptoms you track as Flare-Ups or Daily',group:'tracking',body:'Manage the symptoms you log. Choose Daily for routine check-ins or Flare-Ups for symptoms you record when they occur.'},
 beverages:{title:'Beverages',icon:'cup-soda',summary:'Beverages, volume units, and serving sizes',group:'tracking',body:'Manage the beverages available when logging, their serving sizes, and your preferred volume unit.',conditional:'beverages'},
 activity:{title:'Activity Types',icon:'dumbbell',summary:'Categories for your activity logs',group:'tracking',body:'Manage the activity categories available when you record a workout or other movement.'},
 sleep:{title:'Sleep',icon:'moon',summary:'Default sleep times and morning reminder',group:'tracking',body:'Choose default times for sleep entries and when to receive a morning reminder.'},
 daily:{title:'Daily Check-In',icon:'calendar-check',summary:'Check-in time and reminder',group:'tracking',body:'Your check-in becomes due at the selected time even if its reminder is off.'},
 cycle:{title:'Cycle Settings',icon:'calendar-heart',summary:'Birth control, menopause, and past periods',group:'tracking',body:'Manage cycle preferences when cycle tracking is available and enabled. Cycle information stays outside cloud AI.',conditional:'cycle'},
 meals:{title:'Saved Meals',icon:'utensils',summary:'Meals you reuse in Quick Log',group:'quick',body:'Manage meals you reuse. Saving an item and pinning it as a shortcut remain separate choices.'},
 'saved-activities':{title:'Saved Activities',icon:'dumbbell',summary:'Activities you reuse in Quick Log',group:'quick',body:'Manage reusable activities for Quick Log. Widget pins are managed in Quick Capture.'},
 bowel:{title:'Saved Bowel Movements',icon:'toilet',summary:'Reusable bowel movement entries',group:'quick',body:'Manage saved bowel movement entries. Their discreet widget and watch labels remain unchanged.',conditional:'bowel'},
 capture:{title:'Quick Capture',icon:'zap',summary:'Widget pins, learned habits, and suggestions',group:'quick',body:'Choose pinned shortcuts, manage learned habits and hidden suggestions, and review widget privacy options.'},
 identity:{title:'Account',icon:'user-round',summary:'Your sign-in details',group:'account',body:'Account identity remains separate from your health profile.'},
 security:{title:'Sign-In Security',icon:'shield-check',summary:'Managed by your sign-in provider',group:'account',body:'Your sign-in provider manages authentication. Manage sign-in security through your provider.'},
 export:{title:'Export My Data',icon:'download',summary:'Create a copy of your information',group:'account',body:'Export your account’s data using the existing export and share flow. Review its scope before sharing.'},
 privacy:{title:'Privacy Policy',icon:'shield-check',summary:'How Plectara handles information',group:'account',body:'The existing Privacy Policy remains available in full from this destination.'},
 terms:{title:'Terms of Use',icon:'file-text',summary:'Rules for using Plectara',group:'account',body:'The existing Terms of Use remain available in full from this destination.'}
};
const health=['profile','tracking','quick'], experience=['ai','reminders','appearance','progress'], data=['connections','account'];
const defaults={version:1,views:{}};let saved=defaults;
const models=[];
Object.assign(config,window.referenceScene.config||{});
const activePhone=root.querySelector('.phone');
const startKey=activePhone.dataset.layout+'-'+activePhone.dataset.theme;
saved={version:1,views:{[startKey]:{route:window.referenceScene.route||'home',stack:[],example:window.referenceScene.example||{}}}};
function E(tag,cls,text,attrs={}){const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined&&text!==null)n.textContent=text;Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,v));return n;}
function icon(name,cls=''){const el=E('i',cls,null,{'data-lucide':name,'aria-hidden':'true'});return el;}
function active(id){const i=items[id];return !i?.conditional||config[i.conditional];}
function save(){}
function icons(){if(window.lucide)lucide.createIcons({attrs:{width:22,height:22,'stroke-width':1.8}});}
function row(m,id,small=false){const s=sections[id]||items[id],navigable=!!sections[id],b=E(navigable?'button':'div','setting-row'+(navigable?' cursor-interaction':''),null,navigable?{type:'button','data-route':id}:{'data-destination':id});const symbol=E('span','symbol'+(id==='ai'?' ai':''));symbol.append(icon(s.icon));b.append(symbol);const c=E('span','setting-copy');c.append(E('span','setting-title',s.title));if(!small&&config.descriptions)c.append(E('span','setting-summary',s.summary));b.append(c);if(id==='appearance')b.append(E('span','value',m.example.appearance));b.append(icon('chevron-right','chevron'));if(navigable)b.addEventListener('click',()=>go(m,id));return b;}
function panel(title){const p=E('section','panel panel-list');if(title)p.append(E('h3','',title));return p;}
function group(m,title,ids,small=false){const p=panel(title);ids.filter(active).forEach(id=>p.append(row(m,id,small)));return p;}
function go(m,id){m.stack.push({route:m.route,scroll:m.main.scrollTop});m.route=id;render(m);m.main.scrollTop=0;save();}
function back(m){const prev=m.stack.pop();m.route=prev?.route||'home';render(m);m.main.scrollTop=prev?.scroll||0;save();}
function toggle(m,label,body,key){const wrap=E('label','toggle-row cursor-interaction');const c=E('span','setting-copy');c.append(E('span','setting-title',label));if(body)c.append(E('span','setting-summary',body));const input=E('input','',null,{type:'checkbox',role:'switch','aria-label':label});input.checked=m.example[key];input.addEventListener('change',()=>{m.example[key]=input.checked;save();});wrap.append(c,input);return wrap;}
function introCard(s){const p=E('section','panel');const h=E('div','section-identity');const symbol=E('span','symbol');symbol.append(icon(s.icon));h.append(symbol,E('h3','',s.title));p.append(h,E('p','intro',s.intro));return p;}
function disclosure(title,body){const d=E('details');d.append(E('summary','cursor-interaction',title),E('p','',body));return d;}
function render(m){const s=sections[m.route]||items[m.route];m.title.textContent=s?.title||'Preferences';m.back.setAttribute('aria-label',m.route==='home'?'Close Preferences preview':'Back');m.main.replaceChildren();m.phone.classList.toggle('plain',!config.descriptions);m.phone.style.setProperty('--p-scale',config.textScale);
 if(m.route==='home'){
  if(m.layout==='hub'){m.main.append(group(m,'Your Health',health),group(m,'Settings',experience),group(m,'Connections & Account',data));}
  else{m.main.append(group(m,'Health Profile',['goals','about','conditions','medications'],true),group(m,'Tracking & Routines',['track','symptoms','beverages','activity','sleep','daily','cycle'],true),group(m,'Quick Log & Widgets',['meals','saved-activities','bowel','capture'],true),group(m,'Settings',experience,true),group(m,'Connections & Account',['connections','account'],true));}
 }else if(m.route==='ai'){
  const p=E('section','panel');p.append(E('p','intro','On-device insights keep working whether cloud AI is on or off. With your permission, Plectara sends structured findings to OpenAI with names removed.'));
  m.main.append(p);const ai=panel('Optional Cloud AI');ai.append(toggle(m,'Explanations & Plans','Daily explanations and AI-drafted plans.','narrative'),toggle(m,'Chat About Insights','Follow-up questions and structured findings.','chat'));m.main.append(ai);
  const sharing=panel('Additional Sharing');sharing.append(toggle(m,'Include Alcohol in AI Insights','Off by default. When off, alcohol findings stay on this device.','alcohol'));m.main.append(sharing);
  const privacy=E('section','panel');privacy.append(disclosure('What Is Shared','Structured findings, selected plan context, and—when chat is enabled—questions and recent conversation. The existing consent screen explains the recipient, purpose, frequency, and exclusions before opt-in.'),disclosure('What Stays on This Device','Full diary records, notes, photos, cycle information, and account passwords are excluded from cloud AI. Existing exclusions for wellbeing information continue to apply.'),disclosure('Your Choices','Explanations and plans, chat, and alcohol sharing remain separate choices. Turning cloud AI off does not turn local findings off.'));m.main.append(privacy);
 }else if(m.route==='reminders'){
  const p=panel('Notifications');p.append(toggle(m,'Allow Reminders','Sleep, medication, and check-in notifications.','reminders'));m.main.append(p);
  const timings=panel('Reminder Times');[{id:'sleep',label:'Morning Sleep Reminder',summary:'Sleep'},{id:'medications',label:'Medication Reminders',summary:'Your medication schedules'},{id:'daily',label:'Daily Check-In',summary:'Check-in time and reminder'}].forEach(r=>{const b=row(m,r.id,true);b.querySelector('.setting-title').textContent=r.label;b.querySelector('.setting-copy').append(E('span','setting-summary',r.summary));timings.append(b);});m.main.append(timings);
  const n=E('section','panel notice');n.append(E('h3','', 'One Set of Reminder Settings'),E('p','intro','Changes here also apply in Sleep, Medications, and Daily Check-In. Turning notifications off keeps your schedules and check-in times.'));m.main.append(n);
  const w=E('section','panel');w.append(E('h3','', 'Weekly Check-In'),E('p','intro','Weekly reminders also follow Allow Reminders.'));m.main.append(w);
 }else if(m.route==='appearance'){
  const p=panel('Color Theme');[['System','Match your device'],['Light','Always use light appearance'],['Dark','Always use dark appearance']].forEach(([name,description])=>{const label=E('label','radio-row cursor-interaction');const i=E('input','',null,{type:'radio',name:m.key+'-appearance',value:name});i.checked=m.example.appearance===name;i.addEventListener('change',()=>{m.example.appearance=name;if(name!=='System')m.phone.dataset.theme=name.toLowerCase();else m.phone.dataset.theme=m.theme;save();});const c=E('span','setting-copy');c.append(E('span','setting-title',name),E('span','setting-summary',description));label.append(i,c);p.append(label);});m.main.append(p);
 }else if(m.route==='progress'){
  const p=panel('Points, Streaks & Badges');p.append(toggle(m,'Your Progress','Show your progress and award points as you log.','progress'));m.main.append(p);const info=E('section','panel');info.append(E('p','intro','If you turn this on later, only new logs count. Earlier entries are not scored.'));m.main.append(info);
 }else if(m.route==='connections'){
  const p=panel('Connected Health App');p.append(E('p','setting-title','Apple Health'),E('p','setting-summary','Connect to import supported health data.'));m.main.append(p);const info=E('section','panel');info.append(E('p','intro','Review the data types and permissions before connecting. Turning a log type off also stops new imports for that log.'));m.main.append(info);const note=E('section','panel');note.append(E('p','meta','Health connections are optional. You can keep logging without connecting a health app.'));m.main.append(note);
 }else if(s?.groups){m.main.append(introCard(s));s.groups.forEach(([label,ids])=>m.main.append(group(m,label,ids)));
  if(m.route==='tracking'){const p=E('section','panel notice');p.append(E('h3','', 'Looking for Reminder Times?'));const b=row(m,'reminders',true);p.append(b);m.main.append(p);}
  if(m.route==='account'){const p=panel('Privacy Controls');p.append(row(m,'ai'),row(m,'connections'));m.main.append(p);const a=E('section','panel');['Log Out','Delete Account'].forEach((label,i)=>{const b=E('button','action cursor-interaction'+(i?' danger':''),label,{type:'button'});b.addEventListener('click',()=>{m.dialog.textContent='Design preview only. No account changes were made.';m.dialog.hidden=false;});a.append(b);});m.main.append(a);}
 }else if(items[m.route]){m.route='home';render(m);return;}
 icons();
}
root.querySelectorAll('.phone').forEach((phone,index)=>{const theme=phone.dataset.theme,layout=phone.dataset.layout,key=layout+'-'+theme;const old=saved.version===1?saved.views?.[key]:null;const m={phone,key,theme,layout,route:old?.route||'home',stack:old?.stack||[],example:{appearance:'System',narrative:false,chat:false,alcohol:false,reminders:false,progress:true,...old?.example}};if(m.route!=='home'&&!sections[m.route]&&!items[m.route])m.route='home';
 const yarn=E('div','yarn');yarn.append(E('img','',null,{src:'../plectara/textures/plectara-widget-yarn-gentle-focus-v1.webp',alt:''}));const header=E('header','header');const status=E('div','status');status.append(E('span','','9:41'));const symbols=E('span','status-icons');symbols.append(icon('wifi'),icon('battery-full'));status.append(symbols);const toolbar=E('div','toolbar');m.back=E('button','icon-action cursor-interaction',null,{type:'button','aria-label':'Back'});m.back.append(icon('chevron-left'));m.back.addEventListener('click',()=>{if(m.route==='home'){m.dialog.textContent='Preferences opens from the app’s existing header. This preview starts at Preferences.';m.dialog.hidden=false;}else back(m);});m.title=E('h2','','Preferences');toolbar.append(m.back,m.title);header.append(status,toolbar);m.main=E('main','main',null,{'aria-label':'Preferences content'});m.dialog=E('p','meta',null,{role:'status',hidden:''});m.dialog.style.cssText='background:var(--p-surface);padding:10px 14px;';phone.append(yarn,header,m.main,m.dialog,E('div','home-bar'));models.push(m);render(m);
});
})();
