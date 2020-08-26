const topics = {
    "português": "Interpretação de texto; Tipos de predicado; Função sintática dos sintagmas suboracionais; Casos especiais de regência nominal e verbal. Papel semântico e morfossintático dos sintagmas oracionais (as orações substantivas). Oração adjetiva + Função sintática do pronome relativo.",
    "literatura": "Romantismo: Romance urbano; Senhora; Fase condoreira (Castro Alves). Realismo: características e contexto histórico; contos de Machado de Assis.",
    "produção": "Texto dissertativo argumentativo; Elementos relacionais; Coesão referencial.",
    "inglês": "Texto (Compreensão, estratégias...); Pronomes Relativos (todos os casos); Afixos; Parts of Speech",
    "espanhol": "Interpretação de texto; Presente de subjuntivo regular; Presente do subjuntivo irregular; Condicional simples regular; Condicional simples irregular.",
    "arte": "Impressionismo e Pós-Impressionismo.",
    "matemática 1": "Comprimento da circunferência; Área do círculo; Relações métricas no círculo; Polígonos regulares; Área hachurada; Geometria Espacial de Posição.",
    "matemática 2": "Funções trigonométricas; adição de arcos.",
    "química": "Reações orgânicas e Propriedades ácidas e básicas na orgânica.",
    "laborátorio": "Cinética Química: condições para que ocorra a reação; fatores que têm influência na velocidade das reações",
    "biologia": "Reprodução humana e genética Mendeliana", 
    "física": "Espelhos Esféricos, Refração e Lentes esféricas.",
    "história": "Segunda Guerra Mundial",
    "geografia": "Classificação industrial, produção industrial dos estados unidos e china.",
    "sociologia": "Mundos do Trabalho (capítulo 7)"
}
const calendar = {
    "12/08": {
      "Dia": "Quarta-feira",
      "Língua Estrangeira": "13:30 - 14:40"
    },
    "13/08": {
      "Dia": "Quinta-feira",
      "Produção Textual": "15:00 - 17:00"
    },
    "17/08": {
      "Dia": "Segunda-feira",
      "História": "10:10 - 12:40",
      "Geografia": "10:10 - 12:40"
    },
    "19/08": {
      "Dia": "Quarta-feira",
      "Sociologia e Arte": "10:10 - 12:30"
    },
    "21/08": {
      "Dia": "Sexta-feira",
      "Matemática": "10:10 - 12:30"
    },
    "24/08": {
      "Dia": "Segunda-feira",
      "Física": "10:10 - 12:30"
    },
    "25/08": {
      "Dia": "Terça-feira",
      "Português e Literatura": "10:10 - 12:30"
    },
    "31/08": {
      "Dia": "Segunda-feira",
      "Química": "10:10 - 12:30",
      "Biologia": "10:10 - 12:30"
    }
}

const venom = require('venom-bot');

venom.create().then((client) => start(client));

function start(client) {
    client.onMessage((msg) => {
        if (isSubject(msg.body.toLowerCase())) {
            client.sendText(msg.from, topics[msg.body.toLowerCase()]);
        } else if (isDay(msg.body.toLowerCase())) {
            let ans = isDay(msg.body.toLowerCase());
            let str = "";
            if (typeof ans == 'object') {
                for (key of Object.keys(ans)) {
                     str += `${key}: ${ans[key]}`
                }
                client.sendText(msg.from, str);
            } else {
                client.sendText(msg.from, ans);
            }
        } else if (isTeacher(msg.body.toLowerCase())) {

        }
    });
}

function isSubject(msg) {
    return Object.keys(topics).includes(msg);
}

function isDay(msg) {
    array = msg.split(' ');
    if (array[0] == 'dia') {
        if (array.length == 1) {
            return "fala um dia ae meu consagra";
        }
        for (day of Object.keys(calendar)) {
            if (day.includes(array[1])) {
                return calendar[day];
            }
        }
    }
    return "Não consegui encontrar os dados referentes a essa dia...";
}

function isTeacher(msg) {

}
