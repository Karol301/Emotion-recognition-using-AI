from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2Processor
import torch
import torchaudio
import warnings

warnings.filterwarnings("ignore") 

AUDIO_FILE_PATH = r"..."

MODEL_NAME = "Dpngtm/wav2vec2-emotion-recognition"

try:
    model = Wav2Vec2ForSequenceClassification.from_pretrained(MODEL_NAME)
    processor = Wav2Vec2Processor.from_pretrained(MODEL_NAME)
except Exception as e:
    print(f"Błąd ładowania modelu: {e}")
    exit()

print(f"Analiza pliku: {AUDIO_FILE_PATH}")
try:
    speech_array, sampling_rate = torchaudio.load(AUDIO_FILE_PATH)
except Exception as e:
    print(f"Błąd podczas ładowania pliku audio torchaudio: {e}")
    exit()

TARGET_SAMPLING_RATE = 16000

if sampling_rate != TARGET_SAMPLING_RATE:
    resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=TARGET_SAMPLING_RATE)
    speech_array = resampler(speech_array)

if speech_array.shape[0] > 1:
    speech_array = torch.mean(speech_array, dim=0, keepdim=True)

speech_array = speech_array.squeeze().numpy()

inputs = processor(speech_array, sampling_rate=TARGET_SAMPLING_RATE, return_tensors="pt", padding=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1).squeeze()

emotion_labels = ["angry", "calm", "disgust", "fearful", "happy", "neutral", "sad", "surprised"]
results = {}
for i, prob in enumerate(predictions.tolist()):
    results[emotion_labels[i]] = prob * 100

sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

print("-" * 60)
print("Wyniki Prawdopodobieństw Emocji:")
top_emotion = max(sorted_results, key=sorted_results.get)
top_prob = sorted_results[top_emotion]

for label, prob in sorted_results.items():
    if prob > 5.0:
        print(f"   - {label.capitalize()}: {prob:.2f}%{' <-- PRZEWAGA' if label == top_emotion else ''}")

print("-" * 60)
print(f"Przeważająca Emocja: **{top_emotion.upper()}** z pewnością **{top_prob:.2f}%**")
print("-" * 60)