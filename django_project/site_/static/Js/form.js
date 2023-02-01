document.getElementById("formulario").addEventListener("submit", function(event) {
    event.preventDefault();

    // Enviar formulário aqui (exemplo usando jQuery)
    $.ajax({
        type: "POST",
        url: "/enviar/",
        data: $("#formulario").serialize(),
        success: function() {
            // Mostrar mensagem de sucesso aqui
            alert("Formulário enviado com sucesso!");
        }
    });
})