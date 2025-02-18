import pandas as pd

# Dicionário com perguntas organizadas por nível
questions_data = {
    1: [
        ["Quem construiu a arca para sobreviver ao dilúvio?", "Moisés", "Abraão", "Noé", "Davi", 3],
        ["Quantos discípulos Jesus tinha?", "10", "12", "15", "7", 2],
        ["Qual é o primeiro livro da Bíblia?", "Êxodo", "Gênesis", "Salmos", "Apocalipse", 2],
        ["Qual foi o primeiro milagre de Jesus?", "Multiplicação dos pães", "Caminhar sobre as águas", "Transformar água em vinho", "Curar um cego", 3],
        ["Qual apóstolo negou Jesus três vezes?", "João", "Pedro", "Judas", "Tomé", 2],
        ["Qual era a profissão de Mateus antes de seguir Jesus?", "Pescador", "Médico", "Coletor de impostos", "Carpinteiro", 3],
        ["Onde Moisés recebeu os Dez Mandamentos?", "Monte Sinai", "Monte Carmelo", "Monte das Oliveiras", "Monte Sião", 1],
        ["Quem foi jogado na cova dos leões?", "Elias", "Daniel", "Jeremias", "Ezequiel", 2],
        ["Quem foi engolido por um grande peixe?", "Jonas", "Moisés", "Elias", "Paulo", 1],
        ["Quem traiu Jesus por 30 moedas de prata?", "Pedro", "Judas Iscariotes", "Tiago", "Filipe", 2]
    ],
    2: [
        ["Quem foi a primeira pessoa a ver Jesus ressuscitado?", "Pedro", "Maria Madalena", "João", "Tomé", 2],
        ["Qual rei lançou Sadraque, Mesaque e Abednego na fornalha ardente?", "Davi", "Nabucodonosor", "Salomão", "Herodes", 2],
        ["Qual discípulo era conhecido como 'o discípulo amado'?", "João", "Pedro", "Tiago", "André", 1],
        ["Quem escreveu a maioria das cartas do Novo Testamento?", "Paulo", "Pedro", "João", "Lucas", 1],
        ["Quantos dias durou o dilúvio de Noé?", "40", "100", "7", "365", 1],
        ["Quem foi chamado 'amigo de Deus'?", "Moisés", "Abraão", "Davi", "Salomão", 2],
        ["Quem derrotou o gigante Golias?", "Davi", "Saul", "Samuel", "Ezequiel", 1],
        ["Em qual cidade Jesus nasceu?", "Jerusalém", "Belém", "Nazaré", "Egito", 2],
        ["Quem era o governador romano que condenou Jesus à morte?", "Herodes", "Pilatos", "Caifás", "Félix", 2],
        ["Qual foi a última praga que atingiu o Egito antes da libertação dos hebreus?", "Gafanhotos", "Morte dos primogênitos", "Água em sangue", "Chuva de fogo", 2]
    ],
    3: [
        ["Quem foi ressuscitado por Jesus?", "João Batista", "Lázaro", "Pedro", "Elias", 2],
        ["Quantos pães e peixes Jesus usou para alimentar 5.000 pessoas?", "5 pães e 2 peixes", "4 pães e 3 peixes", "2 pães e 5 peixes", "6 pães e 1 peixe", 1],
        ["Quem andou sobre as águas com Jesus?", "Pedro", "João", "Tiago", "Paulo", 1],
        ["Quem foi curado após tocar nas vestes de Jesus?", "Marta", "Maria Madalena", "Mulher com fluxo de sangue", "Susana", 3],
        ["Qual milagre Jesus realizou no casamento em Caná?", "Multiplicação dos pães", "Transformar água em vinho", "Andar sobre as águas", "Curar um paralítico", 2],
        ["Quem Jesus curou à distância apenas com sua palavra?", "Filho do centurião", "Jairo", "Nicodemos", "Pedro", 1],
        ["Quem teve sua visão restaurada após Jesus usar lama e saliva?", "Bartimeu", "Zaqueu", "Nicodemos", "Natanael", 1],
        ["Qual era o nome do cego que Jesus curou em Jericó?", "Nicodemos", "Bartimeu", "Lázaro", "Simão", 2],
        ["Quem Jesus curou ao colocar barro em seus olhos?", "Bartimeu", "O cego de nascença", "Lázaro", "Nicodemos", 2],
        ["Quem tocou na orla do manto de Jesus e foi curada?", "Maria Madalena", "Mulher com fluxo de sangue", "Ester", "Débora", 2]
    ],
     4: [
        ["Quem foi lançado na cova dos leões?", "Elias", "Daniel", "Jeremias", "Ezequiel", 2],
        ["Quem foi o profeta engolido por um grande peixe?", "Jonas", "Moisés", "Elias", "Paulo", 1],
        ["Qual foi o primeiro milagre de Jesus?", "Multiplicação dos pães", "Caminhar sobre as águas", "Transformar água em vinho", "Curar um cego", 3],
        ["Onde Moisés recebeu os Dez Mandamentos?", "Monte Sinai", "Monte Carmelo", "Monte das Oliveiras", "Monte Sião", 1],
        ["Quem foi jogado na fornalha ardente?", "Sadraque, Mesaque e Abednego", "Daniel", "Elias", "Ezequiel", 1],
        ["Quem foi o primeiro rei de Israel?", "Davi", "Saul", "Salomão", "Samuel", 2],
        ["Qual era a profissão de Pedro antes de seguir Jesus?", "Pescador", "Carpinteiro", "Coletor de impostos", "Médico", 1],
        ["Quem traiu Jesus por 30 moedas de prata?", "Pedro", "Judas Iscariotes", "Tiago", "Filipe", 2],
        ["Quem batizou Jesus?", "Pedro", "Paulo", "João Batista", "Tiago", 3],
        ["Quem recebeu a promessa de que sua descendência seria tão numerosa quanto as estrelas?", "Davi", "Abraão", "Isaac", "Jacó", 2]
    ],
    5: [
        ["Qual é o primeiro livro da Bíblia?", "Êxodo", "Gênesis", "Salmos", "Apocalipse", 2],
        ["Qual foi o discípulo que andou sobre as águas com Jesus?", "Pedro", "João", "Tiago", "Tomé", 1],
        ["Quem era o rei de Israel conhecido por sua grande sabedoria?", "Davi", "Salomão", "Saul", "Josué", 2],
        ["Quem escreveu a maioria das cartas do Novo Testamento?", "Pedro", "Paulo", "João", "Tiago", 2],
        ["Quem foi a única mulher juíza de Israel?", "Ana", "Débora", "Rute", "Ester", 2],
        ["Quem reconheceu Jesus como o Messias quando ele ainda era um bebê?", "Ana e Simeão", "Zacarias e Isabel", "Pedro e João", "Marta e Maria", 1],
        ["Quem era o pai de João Batista?", "Zacarias", "José", "Abraão", "Eli", 1],
        ["Quem teve um sonho sobre vacas gordas e magras?", "José", "Daniel", "Faraó", "Nabucodonosor", 3],
        ["Quem foi a primeira pessoa a ver Jesus ressuscitado?", "Pedro", "Maria Madalena", "João", "Marta", 2],
        ["Quem foi vendido como escravo por seus irmãos?", "José", "Davi", "Moisés", "Jacó", 1]
    ],
    6: [
        ["Quem construiu a arca para sobreviver ao dilúvio?", "Moisés", "Abraão", "Noé", "Jacó", 3],
        ["Quantos discípulos Jesus tinha?", "10", "12", "15", "7", 2],
        ["Quem escreveu o livro do Apocalipse?", "Paulo", "Pedro", "João", "Tiago", 3],
        ["Quem subiu ao céu sem morrer?", "Elias e Enoque", "Moisés e Elias", "Davi e Salomão", "Isaías e Jeremias", 1],
        ["Quantos anos Israel ficou no cativeiro na Babilônia?", "50", "70", "100", "40", 2],
        ["Quem era o irmão de Moisés?", "Josué", "Arão", "Elias", "Davi", 2],
        ["Quem era a esposa de Jacó que ele amava?", "Lea", "Rebeca", "Raquel", "Sara", 3],
        ["Quantos dias e noites choveu durante o dilúvio de Noé?", "30", "40", "50", "60", 2],
        ["Quem foi o primeiro mártir cristão?", "Estevão", "Tiago", "Pedro", "Paulo", 1],
        ["Quem cortou a orelha do servo do sumo sacerdote?", "Pedro", "João", "Tiago", "Paulo", 1]
    ],
    7: [
        ["Quem era o discípulo amado de Jesus?", "João", "Pedro", "Tiago", "André", 1],
        ["Quem foi o pai de Jesus na Terra?", "Pedro", "José", "Tiago", "Paulo", 2],
        ["Qual foi o último milagre de Jesus antes de ser crucificado?", "Curar um cego", "Ressuscitar Lázaro", "Restaurar a orelha de Malco", "Transformar água em vinho", 3],
        ["Quem era o profeta conhecido por sua paciência?", "Moisés", "Elias", "Jó", "Jonas", 3],
        ["Quantas pessoas foram alimentadas com cinco pães e dois peixes?", "4000", "5000", "6000", "3000", 2],
        ["Quem era o melhor amigo de Davi?", "Jonas", "Samuel", "Jônatas", "Ezequiel", 3],
        ["Quem era o rei que perseguiu Elias?", "Saul", "Acabe", "Davi", "Nabucodonosor", 2],
        ["Qual era o nome da esposa de Abraão?", "Sara", "Rebeca", "Raquel", "Ana", 1],
        ["Qual rei lançou Daniel na cova dos leões?", "Saul", "Davi", "Nabucodonosor", "Dario", 4],
        ["Quem foi o profeta que chamou fogo do céu?", "Elias", "Moisés", "Jeremias", "Isaías", 1]
    ],
    8: [
        ["Qual rei construiu a Torre de Babel?", "Nimrod", "Salomão", "Davi", "Herodes", 1],
        ["Quem foi a rainha que salvou os judeus na Pérsia?", "Ester", "Débora", "Maria", "Rute", 1],
        ["Quem era o rei mais sábio de Israel?", "Saul", "Salomão", "Davi", "Nabucodonosor", 2],
        ["Qual era o nome da mãe de Samuel?", "Ana", "Sara", "Rebeca", "Marta", 1],
        ["Quem deu os Dez Mandamentos a Moisés?", "Jesus", "Deus", "Abraão", "Elias", 2],
        ["Quem viu uma escada chegando ao céu em um sonho?", "Jacó", "José", "Elias", "Samuel", 1],
        ["Qual discípulo era um zelote?", "Pedro", "Simão", "Tiago", "João", 2],
        ["Quem escreveu o livro de Provérbios?", "Davi", "Salomão", "Moisés", "Elias", 2],
        ["Qual rei foi transformado em animal por Deus?", "Nabucodonosor", "Davi", "Salomão", "Saul", 1],
        ["Quem foi engolido por um grande peixe?", "Jonas", "Moisés", "Elias", "Paulo", 1]
    ],
     9: [
        ["Quantas pragas Deus enviou ao Egito?", "5", "7", "10", "12", 3],
        ["Quem escreveu o Salmo 23?", "Salomão", "Davi", "Moisés", "Isaías", 2],
        ["Quem foi a rainha que salvou os judeus?", "Ester", "Débora", "Rute", "Ana", 1],
        ["Quem foi o discípulo que duvidou da ressurreição de Jesus?", "Pedro", "Tomé", "João", "Judas", 2],
        ["Qual livro da Bíblia fala sobre a criação do mundo?", "Êxodo", "Levítico", "Gênesis", "Números", 3],
        ["Quem era o rei quando Jesus nasceu?", "Herodes", "Davi", "Saul", "Nabucodonosor", 1],
        ["Quem ajudou Jesus a carregar a cruz?", "Pedro", "Simão de Cirene", "João", "Tiago", 2],
        ["Qual era a cidade natal de Jesus?", "Belém", "Jerusalém", "Nazaré", "Cafarnaum", 1],
        ["Quem foi arrebatado ao céu num carro de fogo?", "Moisés", "Elias", "Isaías", "Daniel", 2],
        ["Quantos anos Jesus tinha quando começou seu ministério?", "25", "30", "33", "40", 2]
    ],
    10: [
        ["Quem é considerado o pai da fé?", "Davi", "Abraão", "Moisés", "Isaac", 2],
        ["Quem escreveu o livro de Provérbios?", "Salomão", "Davi", "Moisés", "Paulo", 1],
        ["Quem era o governador romano que condenou Jesus à morte?", "Herodes", "Pilatos", "Félix", "Caifás", 2],
        ["Quem libertou os israelitas do Egito?", "José", "Abraão", "Moisés", "Davi", 3],
        ["Quem foi o primeiro rei de Judá após a divisão do reino?", "Jeroboão", "Roboão", "Josias", "Ezequias", 2],
        ["Qual discípulo foi crucificado de cabeça para baixo?", "Pedro", "João", "Tiago", "André", 1],
        ["Quem profetizou sobre o vale de ossos secos?", "Isaías", "Jeremias", "Ezequiel", "Daniel", 3],
        ["Quem foi jogado no mar durante uma tempestade?", "Paulo", "Jonas", "Pedro", "Moisés", 2],
        ["Quem disse 'Eis-me aqui, envia-me a mim'?", "Moisés", "Isaías", "Elias", "Jeremias", 2],
        ["Quem escreveu o livro de Atos?", "Lucas", "Paulo", "Pedro", "João", 1]
    ]

}

# Criar lista geral de perguntas com o nível correspondente
questions = []
for nivel, perguntas in questions_data.items():
    for pergunta in perguntas:
        questions.append(pergunta + [nivel])  # Adiciona o nível à pergunta


# Criar DataFrame do pandas
df = pd.DataFrame(questions, columns=["Pergunta", "Opção A", "Opção B", "Opção C", "Opção D", "Resposta", "Nível",])

# Salvar no arquivo Excel corretamente
df.to_excel("questions.xlsx", index=False, engine="openpyxl")

print("✅ Perguntas inseridas com sucesso!")
