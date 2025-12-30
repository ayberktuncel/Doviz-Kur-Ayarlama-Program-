# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 01:25:39 2025

@author: Ayberk Tuncel
"""
import streamlit as st
import requests

# Girdilerin Ayarlanması
st.title("💰 Döviz( USD, EUR to TRY ) Çevirme Programı") #Algoritmada TL yerine TRY kullanılır.
st.write("Hoş geldin! Çevirilecek para ve birimini ayarlayınız.")
para_miktarı= st.number_input("Çevrilecek olan miktarı giriniz",value=100.0)
para_birimi=st.selectbox("Para birimini seçiniz",["USD", "EUR"])

#API-JSON kullanımı
if st.button("Hesapla"):
    adres= f"https://api.frankfurter.app/latest?from={para_birimi}&to=TRY" #para birimi değişkenini süslü paranteze almayı unutmayın
    cevap= requests.get(adres)
    cevap_new = cevap.json() #Karmaşık bilgiyi JSON formatına çevirdik.
    st.write(cevap_new)
    #alttaki kodları yazmadan çalıştırırsak kodu cmd aracılığı ile orda json formatında çıktı gözükür. TRY çevirmek için alt başlık olan -rates- seçilir.
    kur= cevap_new["rates"]["TRY"]
    sonuc = para_miktarı * kur
    #sonucu ekrana bastıralım. Tekrar hatırlayalım TRY=TL
    st.write(para_miktarı, para_birimi, "=", sonuc, "TL")
    st.write("Anlık Kur: 1", para_birimi, "=", kur, "TL")

# İmza
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 20px; color: #888;">
    Tasarlayan: <strong>Ayberk Tuncel</strong>
</div>
""", unsafe_allow_html=True)
