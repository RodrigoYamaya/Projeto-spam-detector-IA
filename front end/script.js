async function analisarEmail() {
    const texto = document.getElementById('textoEmail').value.trim();
    const containerResultado = document.getElementById('resultado-container');
    const tituloResultado = document.getElementById('resultado-titulo');
    const detalheResultado = document.getElementById('resultado-detalhe');
    const btn = document.getElementById('btnAnalisar');
    const btnText = document.getElementById('btnText');
    
    if(!texto) {
        alert("Atenção: Insira o conteúdo interceptado para iniciar a varredura.");
        return;
    }

    // Aqui vai ser Estado de carregamento
    btn.disabled = true;
    btnText.innerHTML = "⏳ Processando heurística...";
    containerResultado.style.display = "none";

    try {
        //  Aqui vai Chama a sua API FastAPI
        const resposta = await fetch('http://127.0.0.1:8000/api/analisar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ texto: texto })
        });

        const dados = await resposta.json();

        // Vai restaurar Restaura o botão
        btn.disabled = false;
        btnText.innerHTML = "Nova Varredura";
        containerResultado.style.display = "block";

        // Vamos Atualizar  a interface com termos de segurança
        if (dados.classificacao === "SPAM") {
            containerResultado.className = "status-spam";
            tituloResultado.innerHTML = `⚠️ AMEAÇA DETECTADA (Phishing/Spam)`;
            detalheResultado.innerHTML = `A inteligência artificial identificou padrões maliciosos severos no texto analisado. Ação recomendada: Quarentena e bloqueio do remetente.`;
        } else {
            containerResultado.className = "status-ham";
            tituloResultado.innerHTML = `✅ TRÁFEGO SEGURO (Legítimo)`;
            detalheResultado.innerHTML = `Nenhum padrão anômalo encontrado pela rede neural. O tráfego foi classificado como seguro e liberado.`;
        }
    } catch (erro) {
        btn.disabled = false;
        btnText.innerHTML = "Iniciar Varredura de Segurança";
        alert("Falha de comunicação com o backend (FastAPI). Verifique se o servidor está rodando na porta 8000.");
        console.error(erro);
    }
}