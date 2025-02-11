import streamlit as st
from datetime import date

def avaliar_risco():
    st.title("🔬 Avaliação de Risco - EPC e SAMR")
    st.write("Sistema dinâmico para análise de precauções hospitalares e recomendações clínicas.")

    tabs = st.tabs(["Dados do Utente", "Critérios de Rastreio", "Resultados e Recomendações"])

    with tabs[0]:
        st.subheader("👤 Dados do Utente")
        nome = st.text_input("Nome do Utente:", key="nome_utente")
        idade = st.number_input("Idade do Utente:", min_value=0, max_value=120, step=1, key="idade_utente")
        processo_clinico = st.text_input("Número do Processo Clínico:", key="processo_clinico")
        data_admissao = st.date_input("📅 Data de Admissão Hospitalar:", value=date.today(), key="data_admissao")

    with tabs[1]:
        st.subheader("🏥 Critérios de Rastreio de EPC e SAMR")

        criterios_epc_samr = [
            st.radio("Internamento hospitalar nos últimos 12 meses?", ("", "Sim", "Não"), key="criterio1"),
            st.radio("Internamento em unidades de cuidados continuados/paliativos ou ERPI?", ("", "Sim", "Não"), key="criterio2"),
            st.radio("Hemodiálise crónica?", ("", "Sim", "Não"), key="criterio3"),
            st.radio("Admissão a cuidados de nível II e III?", ("", "Sim", "Não"), key="criterio4"),
            st.radio("Admissão a unidade de hemato-oncologia ou transplantação?", ("", "Sim", "Não"), key="criterio5")
        ]

        if st.button("🔍 Analisar Critérios EPC e SAMR"):
            if all(criterio != "" for criterio in criterios_epc_samr):
                if "Sim" in criterios_epc_samr:
                    st.warning("⚠️ Necessário realização de teste de EPC e SAMR.")
                    st.info("🧪 **Testes necessários:** Zaragatoa retal para EPC e zaragatoa nasal + amostras de ferida (se existir) para SAMR.")
                    st.warning("⚠️ O utente deve ser mantido em isolamento de contacto até ao resultado dos testes.")
                else:
                    st.success("✅ Sem critérios para realização de rastreio.")

        st.subheader("🏥 Critérios de Rastreio Específico para SAMR")

        criterios_samr = 
            st.radio("Presença de dispositivos invasivos?", ("", "Sim", "Não"), key="samr6"),
            st.radio("Utilização de antibióticos nos 6 meses anteriores?", ("", "Sim", "Não"), key="samr7"),
            st.radio("Feridas não cicatrizadas ou crónicas?", ("", "Sim", "Não"), key="samr8"),
            st.radio("Infeção ou colonização por SAMR prévia?", ("", "Sim", "Não"), key="samr9")

        if st.button("🔍 Analisar Critérios SAMR"):
            if all(criterio != "" for criterio in criterios_samr):
                if "Sim" in criterios_samr:
                    st.warning("⚠️ Necessário realização de teste de SAMR.")
                    st.info("🧪 **Testes necessários:** Zaragatoa nasal e amostras de ferida cutânea (se existir) para SAMR.")
                    st.warning("⚠️ O utente deve ser mantido em isolamento de contacto até ao resultado dos testes.")
                else:
                    st.success("✅ Sem critérios para realização de teste SAMR.")

    with tabs[2]:
        st.subheader("📊 Resultados dos Testes de EPC e SAMR")

        resultado_epc = st.radio("Resultado do teste de EPC?", ("", "Positivo", "Negativo"), key="res_epc")
        resultado_samr = st.radio("Resultado do teste de SAMR?", ("", "Positivo", "Negativo"), key="res_samr")

        if st.button("🔍 Analisar Resultados"):
            if resultado_epc == "Positivo" and resultado_samr == "Positivo":
                st.warning("⚠️ EPC e SAMR Positivos - Manter precauções adicionais de isolamento de contacto e realizar descolonização de SAMR.")
                st.info("✔️ **Isolamento de contacto, preferencialmente em quarto individual ou coorte EPC.**")
                st.info("✔️ **Aplicação do protocolo de descolonização de SAMR:**\n - Pelo menos 5 dias consecutivos de:\n - Mupirocina 2% pomada nasal (3x/dia)\n - Banho com toalhetes de gluconato de clorexidina a 2%")
                st.info("✔️ **1º teste de controlo após 48h do fim do protocolo. Se resultado negativo, 2º teste de controlo uma semana depois.**")
                st.warning("⚠️ **Se testes de SAMR continuarem positivos, repetir o protocolo (máximo de 2 cursos durante o internamento).**")

            elif resultado_epc == "Positivo" and resultado_samr == "Negativo":
                st.warning("⚠️ EPC Positivo - Manter precauções adicionais de isolamento de contacto.")
                st.info("✔️ **Isolamento, preferencialmente em quarto individual ou coorte EPC.**")

            elif resultado_epc == "Negativo" and resultado_samr == "Positivo":
                st.warning("⚠️ SAMR Positivo - Manter precauções adicionais de isolamento de contacto e Aplicar protocolo de descolonização.")
                st.info("✔️ **Aplicação do protocolo de descolonização de SAMR:**\n - Pelo menos 5 dias consecutivos de:\n - Mupirocina 2% pomada nasal (3x/dia)\n - Banho com toalhetes de gluconato de clorexidina a 2%")
                st.info("✔️ **1º teste de controlo após 48h do fim do protocolo. Se resultado negativo, 2º teste de controlo uma semana depois.**")
                st.warning("⚠️ **Se testes de SAMR continuarem positivos, repetir o protocolo (máximo de 2 cursos durante o internamento).**")
                st.info("✔️ **Manter precauções até ao resultado de dois testes seriados negativos.**")

            elif resultado_epc == "Negativo" and resultado_samr == "Negativo":
                st.success("✅ EPC e SAMR Negativos - Implementar precauções básicas de controlo de infeção.")

if __name__ == "__main__":
    avaliar_risco()






