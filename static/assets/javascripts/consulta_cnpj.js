const cnpj = document.querySelector('#cnpj');

const showData = (result) => {
    for (const campo in result) {
        if (campo === 'razao_social' && document.querySelector('#razao_social')) {
            document.querySelector("#razao_social").value = result[campo];
        }
    }
};

cep.addEventListener("blur", (e) => {
    let search = cep.value.replace("-", "");
    const options = {
        method: "GET",
        mode: "cors",
        cache: "default"
    };
    fetch(`https://publica.cnpj.ws/cnpj/${search}`, options)
        .then(response => {
            response.json()
                .then(data => showData(data))
        })
        .catch(e => console.log('Deu Erro: ' + e, message));
});
