/*! For license information please see task_diary.js.LICENSE.txt */
(()=>{function t(e){return t="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},t(e)}function e(){"use strict";e=function(){return r};var n,r={},o=Object.prototype,a=o.hasOwnProperty,c=Object.defineProperty||function(t,e,n){t[e]=n.value},i="function"==typeof Symbol?Symbol:{},s=i.iterator||"@@iterator",u=i.asyncIterator||"@@asyncIterator",l=i.toStringTag||"@@toStringTag";function f(t,e,n){return Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}),t[e]}try{f({},"")}catch(n){f=function(t,e,n){return t[e]=n}}function d(t,e,n,r){var o=e&&e.prototype instanceof k?e:k,a=Object.create(o.prototype),i=new B(r||[]);return c(a,"_invoke",{value:j(t,n,i)}),a}function h(t,e,n){try{return{type:"normal",arg:t.call(e,n)}}catch(t){return{type:"throw",arg:t}}}r.wrap=d;var p="suspendedStart",y="suspendedYield",m="executing",v="completed",g={};function k(){}function E(){}function w(){}var b={};f(b,s,(function(){return this}));var S=Object.getPrototypeOf,x=S&&S(S(N([])));x&&x!==o&&a.call(x,s)&&(b=x);var T=w.prototype=k.prototype=Object.create(b);function L(t){["next","throw","return"].forEach((function(e){f(t,e,(function(t){return this._invoke(e,t)}))}))}function I(e,n){function r(o,c,i,s){var u=h(e[o],e,c);if("throw"!==u.type){var l=u.arg,f=l.value;return f&&"object"==t(f)&&a.call(f,"__await")?n.resolve(f.__await).then((function(t){r("next",t,i,s)}),(function(t){r("throw",t,i,s)})):n.resolve(f).then((function(t){l.value=t,i(l)}),(function(t){return r("throw",t,i,s)}))}s(u.arg)}var o;c(this,"_invoke",{value:function(t,e){function a(){return new n((function(n,o){r(t,e,n,o)}))}return o=o?o.then(a,a):a()}})}function j(t,e,r){var o=p;return function(a,c){if(o===m)throw Error("Generator is already running");if(o===v){if("throw"===a)throw c;return{value:n,done:!0}}for(r.method=a,r.arg=c;;){var i=r.delegate;if(i){var s=O(i,r);if(s){if(s===g)continue;return s}}if("next"===r.method)r.sent=r._sent=r.arg;else if("throw"===r.method){if(o===p)throw o=v,r.arg;r.dispatchException(r.arg)}else"return"===r.method&&r.abrupt("return",r.arg);o=m;var u=h(t,e,r);if("normal"===u.type){if(o=r.done?v:y,u.arg===g)continue;return{value:u.arg,done:r.done}}"throw"===u.type&&(o=v,r.method="throw",r.arg=u.arg)}}}function O(t,e){var r=e.method,o=t.iterator[r];if(o===n)return e.delegate=null,"throw"===r&&t.iterator.return&&(e.method="return",e.arg=n,O(t,e),"throw"===e.method)||"return"!==r&&(e.method="throw",e.arg=new TypeError("The iterator does not provide a '"+r+"' method")),g;var a=h(o,t.iterator,e.arg);if("throw"===a.type)return e.method="throw",e.arg=a.arg,e.delegate=null,g;var c=a.arg;return c?c.done?(e[t.resultName]=c.value,e.next=t.nextLoc,"return"!==e.method&&(e.method="next",e.arg=n),e.delegate=null,g):c:(e.method="throw",e.arg=new TypeError("iterator result is not an object"),e.delegate=null,g)}function C(t){var e={tryLoc:t[0]};1 in t&&(e.catchLoc=t[1]),2 in t&&(e.finallyLoc=t[2],e.afterLoc=t[3]),this.tryEntries.push(e)}function _(t){var e=t.completion||{};e.type="normal",delete e.arg,t.completion=e}function B(t){this.tryEntries=[{tryLoc:"root"}],t.forEach(C,this),this.reset(!0)}function N(e){if(e||""===e){var r=e[s];if(r)return r.call(e);if("function"==typeof e.next)return e;if(!isNaN(e.length)){var o=-1,c=function t(){for(;++o<e.length;)if(a.call(e,o))return t.value=e[o],t.done=!1,t;return t.value=n,t.done=!0,t};return c.next=c}}throw new TypeError(t(e)+" is not iterable")}return E.prototype=w,c(T,"constructor",{value:w,configurable:!0}),c(w,"constructor",{value:E,configurable:!0}),E.displayName=f(w,l,"GeneratorFunction"),r.isGeneratorFunction=function(t){var e="function"==typeof t&&t.constructor;return!!e&&(e===E||"GeneratorFunction"===(e.displayName||e.name))},r.mark=function(t){return Object.setPrototypeOf?Object.setPrototypeOf(t,w):(t.__proto__=w,f(t,l,"GeneratorFunction")),t.prototype=Object.create(T),t},r.awrap=function(t){return{__await:t}},L(I.prototype),f(I.prototype,u,(function(){return this})),r.AsyncIterator=I,r.async=function(t,e,n,o,a){void 0===a&&(a=Promise);var c=new I(d(t,e,n,o),a);return r.isGeneratorFunction(e)?c:c.next().then((function(t){return t.done?t.value:c.next()}))},L(T),f(T,l,"Generator"),f(T,s,(function(){return this})),f(T,"toString",(function(){return"[object Generator]"})),r.keys=function(t){var e=Object(t),n=[];for(var r in e)n.push(r);return n.reverse(),function t(){for(;n.length;){var r=n.pop();if(r in e)return t.value=r,t.done=!1,t}return t.done=!0,t}},r.values=N,B.prototype={constructor:B,reset:function(t){if(this.prev=0,this.next=0,this.sent=this._sent=n,this.done=!1,this.delegate=null,this.method="next",this.arg=n,this.tryEntries.forEach(_),!t)for(var e in this)"t"===e.charAt(0)&&a.call(this,e)&&!isNaN(+e.slice(1))&&(this[e]=n)},stop:function(){this.done=!0;var t=this.tryEntries[0].completion;if("throw"===t.type)throw t.arg;return this.rval},dispatchException:function(t){if(this.done)throw t;var e=this;function r(r,o){return i.type="throw",i.arg=t,e.next=r,o&&(e.method="next",e.arg=n),!!o}for(var o=this.tryEntries.length-1;o>=0;--o){var c=this.tryEntries[o],i=c.completion;if("root"===c.tryLoc)return r("end");if(c.tryLoc<=this.prev){var s=a.call(c,"catchLoc"),u=a.call(c,"finallyLoc");if(s&&u){if(this.prev<c.catchLoc)return r(c.catchLoc,!0);if(this.prev<c.finallyLoc)return r(c.finallyLoc)}else if(s){if(this.prev<c.catchLoc)return r(c.catchLoc,!0)}else{if(!u)throw Error("try statement without catch or finally");if(this.prev<c.finallyLoc)return r(c.finallyLoc)}}}},abrupt:function(t,e){for(var n=this.tryEntries.length-1;n>=0;--n){var r=this.tryEntries[n];if(r.tryLoc<=this.prev&&a.call(r,"finallyLoc")&&this.prev<r.finallyLoc){var o=r;break}}o&&("break"===t||"continue"===t)&&o.tryLoc<=e&&e<=o.finallyLoc&&(o=null);var c=o?o.completion:{};return c.type=t,c.arg=e,o?(this.method="next",this.next=o.finallyLoc,g):this.complete(c)},complete:function(t,e){if("throw"===t.type)throw t.arg;return"break"===t.type||"continue"===t.type?this.next=t.arg:"return"===t.type?(this.rval=this.arg=t.arg,this.method="return",this.next="end"):"normal"===t.type&&e&&(this.next=e),g},finish:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var n=this.tryEntries[e];if(n.finallyLoc===t)return this.complete(n.completion,n.afterLoc),_(n),g}},catch:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var n=this.tryEntries[e];if(n.tryLoc===t){var r=n.completion;if("throw"===r.type){var o=r.arg;_(n)}return o}}throw Error("illegal catch attempt")},delegateYield:function(t,e,r){return this.delegate={iterator:N(t),resultName:e,nextLoc:r},"next"===this.method&&(this.arg=n),g}},r}function n(t,e,n,r,o,a,c){try{var i=t[a](c),s=i.value}catch(t){return void n(t)}i.done?e(s):Promise.resolve(s).then(r,o)}function r(t){return function(){var e=this,r=arguments;return new Promise((function(o,a){var c=t.apply(e,r);function i(t){n(c,o,a,i,s,"next",t)}function s(t){n(c,o,a,i,s,"throw",t)}i(void 0)}))}}function o(t,e){return s(t)||function(t,e){var n=null==t?null:"undefined"!=typeof Symbol&&t[Symbol.iterator]||t["@@iterator"];if(null!=n){var r,o,a,c,i=[],s=!0,u=!1;try{if(a=(n=n.call(t)).next,0===e){if(Object(n)!==n)return;s=!1}else for(;!(s=(r=a.call(n)).done)&&(i.push(r.value),i.length!==e);s=!0);}catch(t){u=!0,o=t}finally{try{if(!s&&null!=n.return&&(c=n.return(),Object(c)!==c))return}finally{if(u)throw o}}return i}}(t,e)||c(t,e)||a()}function a(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function c(t,e){if(t){if("string"==typeof t)return i(t,e);var n={}.toString.call(t).slice(8,-1);return"Object"===n&&t.constructor&&(n=t.constructor.name),"Map"===n||"Set"===n?Array.from(t):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?i(t,e):void 0}}function i(t,e){(null==e||e>t.length)&&(e=t.length);for(var n=0,r=Array(e);n<e;n++)r[n]=t[n];return r}function s(t){if(Array.isArray(t))return t}document.addEventListener("DOMContentLoaded",(function(){var t=document.getElementById("task-form"),n=document.getElementById("task-date"),i=document.getElementById("start-time"),u=document.getElementById("end-time"),l=document.getElementById("task-desc"),f=document.getElementById("tasks-list"),d=document.getElementById("save-button"),h=document.getElementById("entries-container");if(t&&n&&i&&u&&l&&f&&d&&h){document.querySelectorAll(".tabs .tab").forEach((function(t){t.addEventListener("click",(function(){var t=this.dataset.tab;console.log("Tab clicked: ".concat(t)),"today"===t?v():"tomorrow"===t&&k()}))})),t.addEventListener("submit",(function(t){t.preventDefault();var e=n.value,r=i.value,o=u.value,a=l.value;if(e&&a){var c=document.createElement("li");c.textContent="".concat(e," ").concat(r,"-").concat(o,": ").concat(a),c.dataset.status="pending",f.appendChild(c),n.value="",i.value="",u.value="",l.value=""}})),d.addEventListener("click",(function(t){t.preventDefault();var e=[];f.querySelectorAll("li").forEach((function(t){var n,r=s(n=t.textContent.split(": "))||function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)}(n)||c(n)||a(),i=r[0],u=r.slice(1),l=o(i.split(" "),2),f=l[0],d=o(l[1].split("-"),2),h=d[0],p=d[1],y=u.join(": ");e.push({date:f,start_time:h,end_time:p,task_description:y})})),fetch("/task-diary",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({tasks:e,reflections:""})}).then((function(t){if(!t.ok)throw new Error("Network response was not ok");return t.json()})).then((function(t){t.success?(alert("Task diary entry saved!"),b()):alert("Error saving task diary entry.")})).catch((function(t){console.error("There was a problem with the fetch operation:",t)}))}));var p=[];document.getElementById("move-tasks-button").addEventListener("click",(function(){var t=document.getElementById("pending-tasks-list"),e=[],n=[];if(t.querySelectorAll("li").forEach((function(t){var r=t.querySelector('input[type="checkbox"]');r&&r.checked?e.push(parseInt(r.value)):n.push(t)})),0!==e.length){var r=(new Date).toISOString().split("T")[0],o={task_ids:e,date:r};console.log("Payload being sent:",o),fetch("/tasks/select",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(o)}).then((function(t){return t.json()})).then((function(t){if(t.message){p=e;var r=document.getElementById("closed-tasks-list"),o=document.getElementById("pending-tasks-list");e.forEach((function(t){var e=document.querySelector('input[value="'.concat(t,'"]'));if(e){var n=e.parentElement;n&&(n.querySelector('input[type="checkbox"]').checked=!1,r.appendChild(n))}})),o.innerHTML="",n.forEach((function(t){return o.appendChild(t)}))}else alert("Error closing tasks")})).catch((function(t){console.error("Error:",t)}))}else alert("No tasks selected to move.")})),document.getElementById("undo-move-button").addEventListener("click",(function(){var t=document.getElementById("closed-tasks-list"),e=[],n=[];t.querySelectorAll("li").forEach((function(t){var r=t.querySelector('input[type="checkbox"]');r&&r.checked?e.push(parseInt(r.value)):n.push(t)})),console.log("Reverting task IDs:",e),0!==e.length?fetch("/tasks/revert",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({task_ids:e})}).then((function(t){return t.json()})).then((function(r){if(r.message){console.log("Tasks reverted successfully:",r.message);var o=document.getElementById("pending-tasks-list");e.forEach((function(t){var e=document.querySelector('input[value="'.concat(t,'"]'));if(e){var n=e.parentElement;n&&(n.querySelector('input[type="checkbox"]').checked=!1,o.appendChild(n))}})),p=p.filter((function(t){return!e.includes(t)})),t.innerHTML="",n.forEach((function(e){return t.appendChild(e)}))}else console.error("Error reverting tasks:",r.error),alert("Error reverting tasks")})).catch((function(t){console.error("Fetch error:",t),alert("Error reverting tasks")})):alert("No tasks selected to revert.")})),document.getElementById("move-tasks-button-tomorrow").addEventListener("click",(function(){var t=document.getElementById("tomorrow-pending-tasks-list"),e=[],n=[];if(t.querySelectorAll("li").forEach((function(t){var r=t.querySelector('input[type="checkbox"]');r&&r.checked?e.push(parseInt(r.value)):n.push(t)})),0!==e.length){var r={task_ids:e};console.log("Payload being sent:",JSON.stringify(r)),fetch("/tasks/select",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(r)}).then((function(t){return t.json()})).then((function(t){if(t.message){var r=document.getElementById("tomorrow-closed-tasks-list"),o=document.getElementById("tomorrow-pending-tasks-list");e.forEach((function(t){var e=document.querySelector('input[value="'.concat(t,'"]'));if(e){var n=e.parentElement;n&&(n.querySelector('input[type="checkbox"]').checked=!1,r.appendChild(n))}})),o.innerHTML="",n.forEach((function(t){return o.appendChild(t)}))}else alert("Error closing tasks")})).catch((function(t){console.error("Error:",t)}))}else alert("No tasks selected to move.")})),document.getElementById("undo-move-button-tomorrow").addEventListener("click",(function(){var t=document.getElementById("tomorrow-closed-tasks-list"),e=[],n=[];t.querySelectorAll("li").forEach((function(t){var r=t.querySelector('input[type="checkbox"]');r&&r.checked?e.push(parseInt(r.value)):n.push(t)})),0!==e.length?fetch("/tasks/revert",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({task_ids:e})}).then((function(t){return t.json()})).then((function(r){if(r.message){var o=document.getElementById("tomorrow-pending-tasks-list");e.forEach((function(t){var e=document.querySelector('input[value="'.concat(t,'"]'));if(e){var n=e.parentElement;n&&(n.querySelector('input[type="checkbox"]').checked=!1,o.appendChild(n))}})),p=p.filter((function(t){return!e.includes(t)})),t.innerHTML="",n.forEach((function(e){return t.appendChild(e)}))}else console.error("Error reverting tasks:",r.error),alert("Error reverting tasks")})).catch((function(t){console.error("Fetch error:",t),alert("Error reverting tasks")})):alert("No tasks selected to revert.")})),b(),window.viewTasksForDate=function(){return y.apply(this,arguments)},window.selectTasksForDate=function(){return m.apply(this,arguments)},window.fetchTodayTasks=v,window.fetchTomorrowTasks=k}else console.error("One or more elements are missing from the DOM");function y(){return(y=r(e().mark((function t(){var n,r,o,a;return e().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return n=document.getElementById("task-date").value,t.next=3,fetch("/tasks?date=".concat(n));case 3:return r=t.sent,t.next=6,r.json();case 6:o=t.sent,(a=document.getElementById("tasks-for-date")).innerHTML="",o.forEach((function(t){var e=document.createElement("div");e.textContent=t.task_description+("selected"===t.status?" (Selected)":""),a.appendChild(e)}));case 10:case"end":return t.stop()}}),t)})))).apply(this,arguments)}function m(){return m=r(e().mark((function t(){var n,r,o;return e().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:console.log("selectTasksForDate function called"),n=document.getElementById("today-tasks-list"),r=[],n.querySelectorAll("li").forEach((function(t){var e=t.querySelector('input[type="checkbox"]'),n=t.dataset.status;e.checked&&"pending"===n&&r.push(parseInt(e.value))})),console.log("Selected task IDs:",r),o={task_ids:r},console.log("Payload being sent to /tasks/select:",JSON.stringify(o)),fetch("/tasks/select",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(o)}).then((function(t){return console.log("Response from /tasks/select:",t),t.json()})).then((function(t){console.log("Data from /tasks/select:",t),t.message?(alert(t.message),r.forEach((function(t){document.querySelector('input[value="'.concat(t,'"]')).parentElement.dataset.status="selected"}))):t.error?alert("Error: ".concat(t.error)):alert("Unknown error occurred.")})).catch((function(t){console.error("Error:",t)}));case 8:case"end":return t.stop()}}),t)}))),m.apply(this,arguments)}function v(){return g.apply(this,arguments)}function g(){return(g=r(e().mark((function t(){var n,r,o,a;return e().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return console.log("fetchTodayTasks"),t.prev=1,t.next=4,fetch("/tasks/today");case 4:return n=t.sent,t.next=7,n.json();case 7:r=t.sent,o=r.filter((function(t){return"pending"===t.status})),a=r.filter((function(t){return"selected"===t.status})),p=a.map((function(t){return t.id})),w(o,"pending-tasks-list"),w(a,"closed-tasks-list"),t.next=18;break;case 15:t.prev=15,t.t0=t.catch(1),console.error("Error fetching today's tasks:",t.t0);case 18:case"end":return t.stop()}}),t,null,[[1,15]])})))).apply(this,arguments)}function k(){return E.apply(this,arguments)}function E(){return(E=r(e().mark((function t(){var n,r,o,a;return e().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return console.log("fetchTomorrowTasks"),t.prev=1,t.next=4,fetch("/tasks/tomorrow");case 4:return n=t.sent,t.next=7,n.json();case 7:r=t.sent,o=r.filter((function(t){return"pending"===t.status})),a=r.filter((function(t){return"selected"===t.status})),p=a.map((function(t){return t.id})),w(o,"tomorrow-pending-tasks-list"),w(a,"tomorrow-closed-tasks-list"),t.next=18;break;case 15:t.prev=15,t.t0=t.catch(1),console.error("Error fetching tomorrow's tasks:",t.t0);case 18:case"end":return t.stop()}}),t,null,[[1,15]])})))).apply(this,arguments)}function w(t,e){var n=document.getElementById(e);n.innerHTML="",t.forEach((function(t){var e=document.createElement("li"),r=document.createElement("input");r.type="checkbox",r.value=t.id,e.dataset.status=t.status,e.appendChild(r),e.appendChild(document.createTextNode("".concat(t.task_description," (").concat(t.start_time," - ").concat(t.end_time,")"))),n.appendChild(e)}))}function b(){fetch("/get-task-diary-entries").then((function(t){return t.json()})).then((function(t){h.innerHTML="",t.forEach((function(t){var e=document.createElement("div");e.classList.add("entry");var n=document.createElement("h3");n.innerText="Date: ".concat(t.date),e.appendChild(n);var r=document.createElement("p"),o=t.tasks&&Array.isArray(t.tasks)?t.tasks.join(", "):"No tasks available";r.innerText="Tasks: ".concat(o),e.appendChild(r),h.appendChild(e)}))}))}}))})();