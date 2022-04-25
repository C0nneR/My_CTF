#include <stdio.h>
#include <stdint.h>
#include <intrin.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

#define DELTA 0x9e3779b9
#define MX (((z>>6^y<<2) + (y>>3^z<<4)) ^ ((sum^y) + (key[(p&3)^e] ^ z)))

//static char encoding_table[] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
//                                 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
//                                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
//                                 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
//                                 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
//                                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
//                                 'w', 'x', 'y', 'z', '0', '1', '2', '3',
//                                 '4', '5', '6', '7', '8', '9', '+', '/' };
//static int mod_table[] = {0, 2, 1};

static const unsigned char decoding_table[] = {
    66,66,66,66,66,66,66,66,66,66,64,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
    66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,62,66,66,66,63,52,53,
    54,55,56,57,58,59,60,61,66,66,66,65,66,66,66, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,66,66,66,66,66,66,26,27,28,
    29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,66,66,
    66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
    66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
    66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
    66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
    66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
    66,66,66,66,66,66
};

static const uint32_t cipher[] = {
    0x4b6b89a1, 0x74c15453, 0x4092a06e, 0x429b0c07, 0x40281e84, 0x8b5b44c9, 0x66feb37b, 0x3c77a603, 0x79c5892d, 0xd7ada97, 0x1d51aa56, 0x2d4d703, 0x4fa526ba, 0x32fad64a, 0xc0f6091, 0x562b7593, 0xdb9add67, 0x76165563, 0xa5f79315, 0x3aeb991d, 0x1ab721d4, 0xaacd9d2c, 0x825c2b27, 0x76a7761a, 0xb4005f18, 0x117f3763, 0x512cc540, 0xc594a16f, 0xd0e24f8c, 0x9ca3e2e9, 0xa9cc2d5, 0x4629e61d, 0x637129e3, 0xca4e8ad7, 0xf5dfaf71, 0x474e68ab, 0x542fbc3a, 0xd6741617, 0xad0dbbe5, 0x62f7bbe3, 0xc8d68c07, 0x880e950e, 0xf80f25ba, 0x767a264c, 0x9a7ce014, 0x5c8bc9ee, 0x5d9ef7d4, 0xb999acde, 0xb2ec8e13, 0xee68232d, 0x927c5fce, 0xc9e3a85d, 0xac74b56b, 0x42b6e712, 0xcd2898da, 0xfcf11c58, 0xf57075ee, 0x5076e678, 0xd4d66a35, 0x95105ab9, 0x1bb04403, 0xb240b959, 0x7b4e261a, 0x23d129d8, 0xf5e752cd, 0x4ea78f70
};

//char* base64_encode(unsigned char* data, size_t input_length, size_t* output_length) {
//    *output_length = 4 * ((input_length + 2) / 3);
//
//    char* encoded_data = (char*)malloc(*output_length + 1);
//    if (encoded_data == NULL) return NULL;
//    encoded_data[*output_length] = '\0';
//
//    for (size_t i = 0, j = 0; i < input_length;) {
//        uint8_t octet_a = i < input_length ? data[i++] : 0;
//        uint8_t octet_b = i < input_length ? data[i++] : 0;
//        uint8_t octet_c = i < input_length ? data[i++] : 0;
//
//        uint32_t triple = (octet_a << 16) + (octet_b << 8) + octet_c;
//
//        encoded_data[j++] = encoding_table[(triple >> 18) & 63];
//        encoded_data[j++] = encoding_table[(triple >> 12) & 63];
//        encoded_data[j++] = encoding_table[(triple >> 6) & 63];
//        encoded_data[j++] = encoding_table[(triple >> 0) & 63];
//    }
//
//    for (int i = 0; i < mod_table[input_length % 3]; i++) {
//        encoded_data[*output_length - 1 - i] = '=';
//    }
//
//    return encoded_data;
//}

unsigned char* base64_decode(const char* data, size_t input_length, size_t* output_length) {
    if (input_length % 4 != 0) return NULL;

    *output_length = input_length / 4 * 3;
    if (data[input_length - 1] == '=') (*output_length)--;
    if (data[input_length - 2] == '=') (*output_length)--;

    unsigned char* decoded_data = (unsigned char*)malloc(*output_length + 1);
    if (decoded_data == NULL) return NULL;
    decoded_data[*output_length] = '\0';

    for (size_t i = 0, j = 0; i < input_length;) {
        uint32_t sextet_a = data[i] == '=' ? 0 & i++ : decoding_table[data[i++]];
        uint32_t sextet_b = data[i] == '=' ? 0 & i++ : decoding_table[data[i++]];
        uint32_t sextet_c = data[i] == '=' ? 0 & i++ : decoding_table[data[i++]];
        uint32_t sextet_d = data[i] == '=' ? 0 & i++ : decoding_table[data[i++]];
        
        uint32_t triple = (sextet_a << 18) + (sextet_b << 12) + (sextet_c << 6) + sextet_d;

    if (j < *output_length) decoded_data[j++] = (triple >> 16) & 0xff;
    if (j < *output_length) decoded_data[j++] = (triple >> 8) & 0xff;
    if (j < *output_length) decoded_data[j++] = (triple >> 0) & 0xff;
    }
    return decoded_data;
}

void xxtea_enc(uint32_t* v, int n, uint32_t const key[4])
{
    uint32_t y, z, sum;
    unsigned p, rounds, e;
    rounds = 6 + 52 / n;
    sum = 0;
    z = v[n - 1];
    do
    {
        sum += DELTA;
        e = (sum >> 2) & 3;
        for (p = 0; p < n - 1; p++)
        {
            y = v[p + 1];
            z = v[p] += MX;
        }
        y = v[0];
        z = v[n - 1] += MX;
    } while (--rounds);
}

//void xxtea_dec(uint32_t* v, int n, uint32_t const key[4])
//{
//    uint32_t y, z, sum;
//    unsigned p, rounds, e;
//    rounds = 6 + 52 / n;
//    sum = rounds * DELTA;
//    y = v[0];
//    do
//    {
//        e = (sum >> 2) & 3;
//        for (p = n - 1; p > 0; p--)
//        {
//            z = v[p - 1];
//            y = v[p] -= MX;
//        }
//        z = v[n - 1];
//        y = v[0] -= MX;
//        sum -= DELTA;
//    } while (--rounds);
//}

int main()
{
    //unsigned char* data = (unsigned char*)"Hello World!";
    //size_t input_size = strlen((const char*)data);
    //char* encoded_data = base64_encode(data, input_size, &input_size);
    //printf("%s\n", encoded_data);

    char encoded[353];
    memset(encoded, '\0', 353);

    printf("please input the shellcode:\n");
    scanf_s("%352s", encoded, (unsigned)_countof(encoded));
    if (strlen(encoded) != 352) {
        printf("shellcode length error\n");
        system("pause");
        return 0;
    }

    size_t decode_size = strlen(encoded);
    unsigned char* decoded_data = base64_decode(encoded, decode_size, &decode_size);
    //for (int i = 0; i < decode_size; i++) {
    //    printf("%2x ", decoded_data[i]);
    //}
    //printf("\n");
    //printf("%d\n", decode_size);
    size_t plain_size = decode_size % 4 == 0 ? decode_size : decode_size / 4 * 4 + 4;
    unsigned char* plain = (unsigned char*)malloc(plain_size);
    if (plain == NULL) return 0;
    memset(plain, '\0', plain_size);
    memcpy_s(plain, plain_size, decoded_data, decode_size);

    for (int i = 0; i < plain_size; i++) {
        plain[i] = _rotl8(plain[i], 3);
    }

    //for (int i = 0; i < plain_size / 4; i++) {
    //    printf("%x\n", ((uint32_t*)plain)[i]);
    //}

    uint32_t const k[4] = { 't', 'o', 'r', 'a' };
    xxtea_enc((uint32_t*)plain, plain_size / 4, k);
    //for (int i = 0; i < plain_size / 4; i++) {
    //    printf("0x%x, ", ((uint32_t*)plain)[i]);
    //}
    //printf("\n");
    //xxtea_dec((uint32_t*)plain, plain_size / 4, k);
    //for (int i = 0; i < plain_size / 4; i++) {
    //    printf("%x\n", ((uint32_t*)plain)[i]);
    //}
    int cnt = 0;
    for (int i = 0; i < plain_size / 4; i++) {
        if (cipher[i] == ((uint32_t*)plain)[i]) {
            cnt++;
        }
    }
    if (cnt != 66) {
        printf("wrong shellcode\n");
        free(decoded_data);
        free(plain);
        system("pause");
        return 0;
    }

    printf("now let's execute the shellcode\n");
    printf("input your flag:\n");

    char flag[15];
    memset(flag, '\0', 15);
    scanf_s("%14s", flag, (unsigned)_countof(flag));
    if (strlen(flag) != 14) {
        printf("length error\n");
        free(decoded_data);
        free(plain);
        system("pause");
        return 0;
    }

    //unsigned char buf[] = {
    //    "\x60\xFC\x68\x4C\x77\x26\x07\x33\xD2\x64\x8B\x52\x30\x8B\x52\x0C\x8B\x52\x14\x8B\x72\x28\x0F\xB7\x4A\x26\x33\xFF\x33\xC0\xAC\x3C\x61\x7C\x02\x2C\x20\xC1\xCF\x0D\x03\xF8\xE2\xF0\x52\x57\x8B\x52\x10\x8B\x42\x3C\x03\xC2\x8B\x40\x78\x85\xC0\x0F\x84\xBE\x00\x00\x00\x03\xC2\x50\x8B\x48\x18\x8B\x58\x20\x03\xDA\x83\xF9\x00\x0F\x84\xA9\x00\x00\x00\x49\x8B\x34\x8B\x03\xF2\x33\xFF\x33\xC0\xAC\xC1\xCF\x0D\x03\xF8\x3A\xC4\x75\xF4\x03\x7C\x24\x04\x3B\x7C\x24\x0C\x75\xD9\x33\xFF\x33\xC9\x83\xC2\x50\x0F\xB6\x04\x0A\xC1\xCF\x0D\x03\xF8\x41\x83\xF9\x0E\x75\xF1\xC1\xCF\x0D\x57\x33\xFF\x33\xC9\x8B\x54\x24\x3C\x52\x0F\xB6\x1C\x0E\xB8\x67\x66\x66\x66\xF7\xEB\xD1\xFA\x8B\xC2\xC1\xE8\x1F\x03\xC2\x8D\x04\x80\x2B\xD8\x5A\x0F\xB6\x04\x0A\x2B\xC3\xC1\xCF\x0D\x03\xF8\x41\x83\xF9\x0E\x75\xD4\xC1\xCF\x0D\x3B\x3C\x24\x74\x16\x68\x25\x73\x00\x00\x8B\xC4\x68\x6E\x6F\x00\x00\x54\x50\x8B\x5C\x24\x48\xFF\xD3\xEB\x14\x68\x25\x73\x00\x00\x8B\xC4\x68\x79\x65\x73\x00\x54\x50\x8B\x5C\x24\x48\xFF\xD3\x58\x58\x58\x58\x58\x58\x58\x58\x58\x61\xC3\x58\x5F\x5A\x8B\x12\xE9\x0B\xFF\xFF\xFF"
    //};

    LPVOID exec = VirtualAlloc(NULL, decode_size, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    if (exec == NULL) return -1;
    CopyMemory(exec, decoded_data, decode_size);

    //LPVOID exec = VirtualAlloc(NULL, sizeof(buf), MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    //if (exec == NULL) return -1;
    //CopyMemory(exec, buf, sizeof(buf));
    
    __asm
    {
        lea eax, flag
        push eax
        lea eax, printf
        push eax
    }

    ((void(*)())exec)();

    __asm
    {
        pop eax
        pop eax
    }

    free(decoded_data);
    free(plain);
    VirtualFree(exec, 0, MEM_RELEASE);

    printf("\nyour final flag is HFCTF{md5(two inputs concated)}\n");
    system("pause");
	return 0;
}