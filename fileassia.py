import assemblyai as aai

aai.settings.api_key = "402b1283f7fe4e839748808d0c8c4ab8"

FILE_URL = "0a01ec79707d42ae815d5d4de5573827.mp3"

transcriber = aai.Transcriber()
configuracoes = aai.TranscriptionConfig(speaker_labels=True, speakers_expected=2,language_code='pt') 
transcript = transcriber.transcribe(FILE_URL, config=configuracoes)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    for utt in transcript.utterances:
        print(f"{utt.speaker}: {utt.text}")
        print('\n')