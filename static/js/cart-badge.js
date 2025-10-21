document.addEventListener('DOMContentLoaded', ()=>{
  const b=document.getElementById('cartCount');
  if(b){ const n=parseInt(b.dataset.count||b.textContent||'0',10)||0;
    b.textContent=n; b.dataset.count=n; }
});