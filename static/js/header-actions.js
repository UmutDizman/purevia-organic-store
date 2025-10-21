

document.addEventListener('DOMContentLoaded', () => {

    const userWrap = document.getElementById('userMenu');
    if (userWrap) {
        const btn = userWrap.querySelector('button');
        const dd = userWrap.querySelector('.dropdown');

        if (btn && dd) {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const open = dd.hasAttribute('hidden');
                document.querySelectorAll('.dropdown').forEach(d => d.setAttribute('hidden', ''));
                if (open) dd.removeAttribute('hidden'); else dd.setAttribute('hidden', '');
                btn.setAttribute('aria-expanded',String(open));

            });
        }
    }


    const st = document.getElementById('searchToggle');
    const sp = document.getElementById('searchPanel');
    if (st && sp) {
        st.addEventListener('click', (e) => {
            e.stopPropagation();
            const open = sp.hasAttribute('hidden');
            document.querySelectorAll('.dropdown, .search-panel').forEach(d => d.setAttribute('hidden',''));
            if (open) sp.removeAttribute('hidden'); else sp.setAttribute('hidden','');
            st.setAttribute('aria-expanded', String(open));
            if (open) setTimeout(() => sp.querySelector('input')?.focus(), 10);
        });

    }

    document.addEventListener('click', () => {
        document.querySelectorAll('.dropdown, .search-panel').forEach(d => d.setAttribute('hidden',''));
        document.querySelectorAll('.icon-btn, .avatar-btn').forEach(b => b.setAttribute('aria-expanded','false'));

    });
});