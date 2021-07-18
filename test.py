from denoise import AudioDeNoise

audioDenoiser = AudioDeNoise(inputFile="input.wav")
audioDenoiser.deNoise(outputFile="input_denoised.wav")