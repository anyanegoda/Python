def get_frames(signal, size, overlap):
    signal = [x for x in range(0, size)]
    frame = 4
    print('Размер фрейма(окна): ', frame)
    step = frame * overlap
    print('Шаг: ',step)
    i = 0
    while i < len(signal):
        yield (signal[i:i + frame])
        i += int(step)

signal = []
print('Оконная декомпозиция:')
for frame in get_frames(signal, size=1024, overlap=0.5):
    print(frame)