import zlib
import bz2
import lzma


'''
def bz2_data_compress(data_to_compress):	-> return compressed_data 
def bz2_data_decompress(compressed_data):	-> return plain_data
def zlib_data_compress(data_to_compress): 	-> return compressed_data 
def zlib_data_decompress(compressed_data):	-> return plain_data
def zlib_file_compress(input_file):		-> return out_file_name
def zlib_file_decompress(compressed_file):	-> return out_file_name
'''


#Write the data to file
def write_to_file(input_data,file_name):
	f = open(file_name, 'wb')
	f.write(input_data)
	f.close()	



def lzma_data_compress(data_to_compress):
	compressed_data = lzma.compress(data_to_compress)
	with lzma.open("file", "wb") as f:
		f.write(compressed_data)
	return compressed_data


def lzma_data_decompress(compressed_data):
	plain_data = lzma.decompress(compressed_data)
	return plain_data



#Compress the data - bz2
def bz2_data_compress(data_to_compress):
	compressed_data  = bz2.compress(data_to_compress)
	return compressed_data

#Decompress the compressed data - bz2
def bz2_data_decompress(compressed_data):
	plain_data = bz2.decompress(compressed_data)
	return plain_data


def bz2_file_compress(input_file_name,output_file_name):
	plan_data=open(input_file_name, 'rb').read()
	output = bz2.BZ2File(output_file_name, 'wb')
	output.write(plan_data)
	output.close()
	return output_file_name


def bz2_file_decompress(compressed_file,output_file_name):
	input_file  = bz2.BZ2File(input_file, 'rb')
	input_file.read()
	input_file.close()
	return output_file_name

#Compress the data - zlib
def zlib_data_compress(data_to_compress):
	compressed_data = zlib.compress(data_to_compress, 2)
	return compressed_data

#Decompress the compressed data - zlib
def zlib_data_decompress(compressed_data):
	plain_data = zlib.decompress(compressed_data)
	return plain_data

#Compress file - zlib
def zlib_file_compress(input_file_name,output_file_name):
	original_data = open(input_file_name, 'rb').read()
	compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)
	write_to_file(compressed_data,output_file_name)
	return output_file_name

#Compress file - zlib
def zlib_file_decompress(compressed_file,output_file_name):
	compressed_data = open(compressed_file, 'rb').read()
	original_data = zlib.decompress(compressed_data)
	write_to_file(original_data,out_file_name)
	return out_file_name
	



my_data = b'Hello world'
compressed_data=lzma_data_compress(my_data)
print(compressed_data)
plain_data=lzma_data_decompress(compressed_data)
print(plain_data)

compressed_data=zlib_data_compress(my_data)
print(compressed_data)
plain_data=zlib_data_decompress(compressed_data)
print(plain_data)
compressed_data=bz2_data_compress(my_data)
print(compressed_data)
plain_data=bz2_data_decompress(compressed_data)
print(plain_data)
out_file_name=zlib_file_compress('Output.xlsx','compressed_file')
print(out_file_name)
out_file_name=zlib_file_decompress('compressed_file','uncompress_file')
print(out_file_name)
