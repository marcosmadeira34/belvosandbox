// requestapi.js
let belvoWidget; // Variável para armazenar a instância do widget
let linkData; // Variável para armazenar as chaves e valores do JSON retornado

function successCallbackFunction(data) {
    // Extrair as informações do JSON retornado
    
    const link = data.id;
    const institution = data.institution;
    // Armazenar o objeto JSON completo em linkData
    linkData = data;          
    // Aqui você pode fazer algo com o link e a instituição,
    // como associá-los ao usuário registrado no seu banco de dados.
    console.log("Link ID:", link);
    console.log("Institution:", institution);                                    
}

function onExitCallbackFunction(data) {
    // Callback de saída (quando o widget é fechado)
    // Implemente o que deseja fazer quando o widget é fechado aqui
}

function onEventCallbackFunction(data) {
    // Callback para outros eventos do widget
    // Implemente o que deseja fazer com outros eventos do widget aqui
}

function openBelvoWidget(accessToken) {
    // Desabilitar o botão durante o processo de integração
    const button = document.getElementById("embedWidgetButton");
    button.disabled = true;
    
    belvoWidget = belvoSDK.createWidget(accessToken, {
        // Configuração do widget
        country_codes: ['BR'],
        locale: 'pt',
        show_abandon_survey: false,
        external_id: '123456789',
        institution_types: ['retail'],
        callback: (data) => {
            // Callback de sucesso
            successCallbackFunction(data);
            const link = data.id;
            const institution = data.institution;
            // Armazenar o objeto JSON completo em linkData
            linkData = data;          
            // Aqui você pode fazer algo com o link e a instituição,
            // como associá-los ao usuário registrado no seu banco de dados.
            console.log("Link ID:", link);
            console.log("Institution:", institution);
            // Exibir mensagem de conclusão
            const statusMessage = document.getElementById("statusMessage");
            statusMessage.textContent = "Integração concluída com sucesso!";
            // incluir uma mensagem de alerta para o usuário informando que a integração foi realizada com sucesso
            statusMessage.classList.add("alert", "alert-success");
            // Habilitar o botão novamente após a conclusão
            button.disabled = false;
        },
        onExit: (data) => {
            // Callback de saída (quando o widget é fechado)
            onExitCallbackFunction(data);
            // Exibir mensagem de cancelamento ou saída
            const statusMessage = document.getElementById("statusMessage");
            statusMessage.textContent = "O processo de incorporação do widget foi cancelado ou fechado.";
            // Habilitar o botão novamente após o cancelamento ou fechamento
            button.disabled = false;
        },
        onEvent: (data) => {
            // Callback para outros eventos do widget
            onEventCallbackFunction(data);
        }
    }).build();
}

// Adiciona o evento de clique ao botão "Começar Integração"
document.getElementById("embedWidgetButton").addEventListener("click", function() {
    // Verifica novamente se o token de acesso está definido globalmente (caso ele não tenha sido passado pelo template)
    if (typeof accessToken !== "undefined") {
        // Se o token de acesso estiver definido, inicializa o widget com o token
        openBelvoWidget(accessToken);
    } else {
        // Caso o token de acesso não esteja definido, exibe uma mensagem de erro
        const statusMessage = document.getElementById("statusMessage");
        statusMessage.textContent = "Erro: Token de acesso não fornecido.";
        // incluir uma mensagem de alerta para o usuário informando que a integração foi realizada com sucesso
    }
});
