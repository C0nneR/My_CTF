#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void decrypt(int32_t v[10]){
    int32_t tea_delta = 22334455;
    int32_t tea_sum = 1592647341 + 100 * tea_delta;
    int32_t tea_key[4] = {21332, 20301, 8308, 25953};

    int32_t xtea_delta = 123456789;
    int32_t xtea_sum = 987654321 + 100 * xtea_delta;
    int32_t xtea_key[4] = {18764, 28534, 25888, 17237};

    for (int i = 8; i >=0; i -= 2){
        int32_t round_max = (i == 0)?19:20;
        int32_t v0 = v[i];
        int32_t v1 = v[i + 1];
        for (int round = round_max - 1; round >= 0; round--){
            v1 -= ((v0 * 16) + tea_key[2]) ^ (v0 + tea_sum) ^ ((v0 / 32) + tea_key[3]);
            v0 -= ((v1 * 16) + tea_key[0]) ^ (v1 + tea_sum) ^ ((v1 / 32) + tea_key[1]);
            tea_sum -= tea_delta;

            v1 -= (((v0 * 16) ^ (v0 / 32)) + v0) ^ (xtea_sum + xtea_key[(xtea_sum / 2048) & 3]);
            xtea_sum -= xtea_delta;
            v0 -= (((v1 * 16) ^ (v1 / 32)) + v1) ^ (xtea_sum + xtea_key[xtea_sum & 3]);
        }
        v[i] = v0;
        v[i + 1] = v1;
    }

    v[1] -= ((v[0] * 16) + tea_key[2]) ^ (v[0] + 1614981796) ^ ((v[0] / 32) + tea_key[3]);
    v[0] -= ((v[1] * 16) + tea_key[0]) ^ (v[1] + 1614981796) ^ ((v[1] / 32) + tea_key[1]);

    for (int i = 0; i < 10; i++){
        v[i] ^= 0x1010101 * (i + 1);
    }

    v[1] -= (((v[0] * 16) ^ (v[0] / 32)) + v[0]) ^ (1111111110 + xtea_key[(1111111110 / 2048) & 3]);
    v[0] -= (((v[1] * 16) ^ (v[1] / 32)) + v[1]) ^ (987654321 + xtea_key[987654321 & 3]);

    for (int i = 0; i < 10; i++){
        v[i] ^= 0x1010101 * (i + 1);
    }

}

int main(){
    int32_t cipher[10] = {0xAEE0FAE8, 0xFC3E4101, 0x167CAD92, 0x51EA6CBE, 0x242A0100, 0x01511A1B, 0x514D6694, 0x2F5FBFEB, 0x46D36398, 0x79EEE3F0};
    decrypt(cipher);
    puts((char*)cipher);
    return 0;
}