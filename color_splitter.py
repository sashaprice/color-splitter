import sys
import copy
from PIL import Image

__SUPPORTED_MODES = {'RGB', 'CMYK', 'HSV', 'YCbCr', 'L'}

# Retrieves arguments from command line
arguments = {}
for token in sys.argv[1:]:
	pair = token.split('=')
	arguments[pair[0]] = pair[1]

file_in = arguments['input']
name_in = file_in[:len(file_in) - 4]
rgb_out = arguments['rgb_out'].lower() == 'true' if 'rgb_out' in arguments else False
ext_out = arguments['output'].lower() if 'output' in arguments else file_in[len(name_in) + 1:]
mode = arguments['space']

if mode in __SUPPORTED_MODES:
	# Retrieves source image converted to output mode
	source = Image.open(file_in).convert(mode=mode)
	dim = source.size

	# Separates each band of source image
	band_names = source.getbands()
	bands = source.split()
	num_bands = len(bands)

	# Default black pixel is all 0; YCbCr uses (0, 128, 128) for black pixel
	black = ([Image.new('L', dim), Image.new('L', dim, 128), Image.new('L', dim, 128)] if mode == 'YCbCr'
			 else [Image.new('L', dim) for unused in range(num_bands)])

	# Reconstructs each channel into image and converts into RGB for viewability
	for i in range(num_bands):
		isolated = copy.deepcopy(black)
		isolated[i] = bands[i]
		
		# Converts image to RGB if enabled to avoid compatibility issues with image format
		output = Image.merge(mode, isolated)
		if rgb_out:
			output = output.convert(mode='RGB')
		
		output.save(name_in + '_' + band_names[i] + '.' + ext_out)