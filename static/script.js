function dispararPipeline() {
    const btn = document.getElementById('btn-push');
    const statusText = document.getElementById('status-text');
    const displayContainer = document.getElementById('display-container');

    btn.disabled = true;

    // commit e CI milho
    displayContainer.innerHTML = '<span id="display-icon" class="step-icon-3d pulse">🌽</span>';
    statusText.innerText = "Commit recebido! Rodando testes na esteira...";

    // bu8ild Docker fogo
    setTimeout(() => {
        displayContainer.innerHTML = '<span id="display-icon" class="step-icon-3d pulse">🔥</span>';
        statusText.innerText = "Gerando imagem Docker...";
    }, 1200);

    //  deploy AWS pipoca
    setTimeout(() => {
        displayContainer.innerHTML = '<img src="/static/balde-pipoca.png" class="pipoca-entregue-img" alt="Pipoca Pronta">';
        statusText.innerText = "Deploy feito na AWS! Pipoca pronta!";
        btn.disabled = false;
    }, 2500);
}