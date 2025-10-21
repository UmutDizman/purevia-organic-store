

document.addEventListener('DOMContentLoaded',function () {
    const container = document.getElementById('django-messages');



    if (container) {
        const messages = JSON.parse(container.dataset.messages || "[]");

    
    if (messages.length > 0) {

        const last = messages[messages.length -1];
        let icon = 'info';
        if (last.tags.includes('success')) icon = 'success';
        else if (last.tags.includes('warning')) icon ='warning';
        else if (last.tags.includes('error') || last.tags.includes('danger')) icon ='error';
        
        const lines = messages.map(m => `• ${m.text}`).join('\n');

        Swal.fire({
            title: '',
            text: lines,
            icon: icon,
            confirmButtonText: 'Tamam',
            timer: 2500,
            timerProgressBar: true

        });
    }
    
    }
});