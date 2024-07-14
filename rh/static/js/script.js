const textarea_habilidades = document.getElementById('habilidades_tecnicas');
const textarea_experiencias = document.getElementById('experiencia_profissional');
const textarea_descricao = document.getElementById('descricao');


textarea_habilidades.addEventListener('focus', function() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight + 15) + 'px';
});

textarea_experiencias.addEventListener('focus', function(){
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight + 15) + 'px';
})

textarea_descricao.addEventListener('focus', function(){
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight + 15) + 'px';
})

function confirmar_exclusao(id_recrutamento){
    return confirm("Tem certeza que deseja excluir o item de ID '"+id_recrutamento+"'? O processo é irreversível!")
}