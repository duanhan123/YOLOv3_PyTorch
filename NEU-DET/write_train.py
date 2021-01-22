import numpy as np

classes = ["crazing_", "inclusion_", "patches_","pitted_surface_","rolled-in_scale_","scratches_"]

for c in classes:
    file = open("train.txt", 'a')
    a = [x for x in range(1,301)]
    np.random.shuffle(a)
    # print(len(a[270:]))
    for i in range(270):
        file.write(c + str(a[i]) + '\n')
    file.close()

    file = open("val.txt", 'a')
    for i in range(270,300):
        file.write(c + str(a[i]) + '\n')
    file.close()
