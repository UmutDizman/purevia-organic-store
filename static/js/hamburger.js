const btn = document.getElementById('navBtn');
const nav = document.getElementById('nav');



function closeMenu(){
    nav.classList.remove('open');
    btn.classList.remove('open');
    btn.setAttribute('aria-expanded','false');
    document.body.classList.remove('body-lock');

}


btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.classList.toggle('open',open);
    btn.setAttribute('aria-expanded',open ? 'true':'false');
    document.body.classList.toggle('body-lock',open);

});
nav.addEventListener('click', e => {if(e.target.tagName === 'A')closeMenu(); });
window.addEventListener('keydown', e => {if(e.key === 'Escape')closeMenu(); });

window.addEventListener('resize', () => {
    if(window.innerWidth > 920) document.body.classList.remove('body-lock');
});