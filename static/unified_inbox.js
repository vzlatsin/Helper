document.addEventListener("DOMContentLoaded",(function(){var e=document.getElementById("capture-button"),t=document.getElementById("capture-modal"),n=document.querySelector(".close-button"),i=document.getElementById("capture-form"),o=document.getElementById("unified-inbox-list"),c=function(){t.style.display="none"};e.addEventListener("click",(function(){t.style.display="block"})),n.addEventListener("click",c),window.addEventListener("click",(function(e){e.target==t&&c()}));var r=function(e,t){var n=document.createElement("li");n.textContent=e,n.dataset.id=t;var i=document.createElement("i");i.className="fas fa-pencil-alt",i.style.marginLeft="10px",i.style.cursor="pointer",i.addEventListener("click",(function(){return d(t,e)}));var c=document.createElement("i");c.className="fas fa-times",c.style.marginLeft="10px",c.style.cursor="pointer",c.addEventListener("click",(function(){return a(t)})),n.appendChild(i),n.appendChild(c),o.appendChild(n)};i.addEventListener("submit",(function(e){e.preventDefault();var t=document.getElementById("capture-description").value;fetch("/unified-inbox",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({description:t})}).then((function(e){return e.json()})).then((function(e){e.id?(r(t,e.id),i.reset(),c()):console.error("Error adding item to inbox:",e.error)}))}));var d=function(e,t){var n=prompt("Edit the description:",t);n&&fetch("/unified-inbox/".concat(e),{method:"PUT",headers:{"Content-Type":"application/json"},body:JSON.stringify({description:n})}).then((function(t){t.ok?document.querySelector("li[data-id='".concat(e,"']")).firstChild.textContent=n:console.error("Failed to update item")}))},a=function(e){fetch("/unified-inbox/".concat(e),{method:"DELETE"}).then((function(t){t.ok?document.querySelector("li[data-id='".concat(e,"']")).remove():console.error("Failed to delete item")}))};fetch("/unified-inbox").then((function(e){return e.json()})).then((function(e){e.forEach((function(e){return r(e.description,e.id)}))}))}));