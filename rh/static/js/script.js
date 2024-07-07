const textarea_habilidades = document.getElementById('habilidades');
const textarea_experiencias = document.getElementById('experiencias_pro');

textarea_habilidades.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight + 15) + 'px';
});

textarea_experiencias.addEventListener('input', function(){
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight + 15) + 'px';
})