# Emotion-recognition-using-AI

Temat:


Rozpoznawanie emocji w głosie za pomocą AI (2025)

Podsumowanie:


Celem projektu było opracowanie i ocena modeli sztucznej inteligencji do rozpoznawania emocji w nagraniach głosowych. Sprawdziliśmy jak różne algorytmy radzą sobie z klasyfikacją emocji. W projekcie wykorzystano zarówno modele akustyczne (np. Dpngtm/wav2vec2-emotion-recognition), jak i multimodalne (Gemini 2.5 Pro oraz Twelve Labs). Do testów użyto bazy danych RAVDESS, a także własnych nagrań wybranych z filmów.

Metodologia:


1.Zbieranie i przygotowanie danych:

Dane pochodzą z bazy RAVDESS, zawierającej nagrania głosowe i wideo aktorów a także przygotowano własne nagrania z filmów.
Pliki zostały znormalizowane i przycięte do odpowiedniej długości.

2.Modele użyte w badaniu:

Dpngtm/wav2vec2-emotion-recognition – model akustyczny oparty na Wav2Vec 2.0.
Gemini 2.5 Pro – multimodalny model AI analizujący zarówno dźwięk, jak i obraz.
Twelve Labs – multimodalny model przetwarzający dane wideo i audio.

3.Procedura testowa:

Dla każdego modelu przygotowano zestaw testowy (2 nagrania z RAVDESS + 2 własne).

Wyniki:


-Dpngtm/wav2vec2-emotion-recognition:

Bardzo dobre wyniki dla danych z bazy RAVDESS (ok. 90% trafności), lecz słabsze dla nagrań własnych (ok. 30%).
Problemy najprawdopodobniej wynikały z obecności szumów i mniej kontrolowanych warunków akustycznych.

-Gemini 2.5 Pro:

Najlepsze wyniki spośród testowanych modeli. Poprawnie klasyfikował emocje zarówno w danych laboratoryjnych, jak i własnych.
Radził sobie również z analizą scen zawierających więcej niż jedną osobę.

-Twelve Labs:
Niższa skuteczność niż Gemini. Często dodawał komentarze lub nie był w stanie jednoznacznie określić emocji.
Najgorzej radził sobie z emocjami: wstręt, strach, złość.
