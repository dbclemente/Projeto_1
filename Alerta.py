#!pip install plyer
from plyer import notifcation

def alerta(nivel, base, etapa):
    if etapa == "inicio": # Para o incio do processo da pipeline
        title = "Pipeline ETL Iniciado"
        message = "Iniciando"

    elif etapa == "fim": # Para o fim do processo da pipeline
        title = "Pipeline ETL Concluído"
        message = "Finalizado"
        
    elif nivel == 0:
        title = "Etapa Concluída"
        message = f"{etapa} da {base} concluída com sucesso."
        
    elif nivel == 1:
        title = "Alerta Baixo"
        message = f"Falha no carregamento {base} na etapa {etapa}"

    elif nivel == 2:
        title = "Alerta Moderado"
        message = f"Falha no carregamento {base} na etapa {etapa}"
    
    elif nivel == 3:
        title = "Alerta Alto"
        message = f"Falha no carregamento {base} na etapa {etapa}"

    else:
        title = "Alerta desconhecido" #Para situaçao de nivel de alerta fora do proposto.
        message = f"Nivel de alerta desconhecido ({nivel}) para {base} na etapa {etapa}"

    notification.notify(
        title=title,
        message=message,
        app_name = "Projeto Final",
        timeout=10
    )



#adicionar a funcao alerta(nivel, base, etapa) em cada etapa