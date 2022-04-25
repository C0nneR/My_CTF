#include <stdio.h>
#include <stdint.h>
#define DELTA 0x9e3779b9
#define MX (((z>>6^y<<2) + (y>>3^z<<4)) ^ ((sum^y) + (key[(p&3)^e] ^ z)))
 
void btea(uint32_t *v, int n, uint32_t const key[4])
{
    uint32_t y, z, sum;
    unsigned p, rounds, e;
    if (n > 1)            /* Coding Part */
    {
        rounds = 6 + 52/n;
        sum = 0;
        z = v[n-1];
        do
        {
            sum += DELTA;
            e = (sum >> 2) & 3;
            for (p=0; p<n-1; p++)
            {
                y = v[p+1];
                z = v[p] += MX;
            }
            y = v[0];
            z = v[n-1] += MX;
        }
        while (--rounds);
    }
    else if (n < -1)      /* Decoding Part */
    {
        n = -n;
        rounds = 6 + 52/n;
        sum = rounds*DELTA;
        y = v[0];
        do
        {
            e = (sum >> 2) & 3;
            for (p=n-1; p>0; p--)
            {
                z = v[p-1];
                y = v[p] -= MX;
            }
            z = v[n-1];
            y = v[0] -= MX;
            sum -= DELTA;
        }
        while (--rounds);
    }
}
 
 
int main()
{
    uint32_t v[66]= {0x4b6b89a1, 0x74c15453, 0x4092a06e, 0x429b0c07, 0x40281e84, 0x8b5b44c9, 0x66feb37b, 0x3c77a603, 0x79c5892d, 0xd7ada97, 0x1d51aa56, 0x2d4d703, 0x4fa526ba, 0x32fad64a, 0xc0f6091, 0x562b7593, 0xdb9add67, 0x76165563, 0xa5f79315, 0x3aeb991d, 0x1ab721d4, 0xaacd9d2c, 0x825c2b27, 0x76a7761a, 0xb4005f18, 0x117f3763, 0x512cc540, 0xc594a16f, 0xd0e24f8c, 0x9ca3e2e9, 0xa9cc2d5, 0x4629e61d, 0x637129e3, 0xca4e8ad7, 0xf5dfaf71, 0x474e68ab, 0x542fbc3a, 0xd6741617, 0xad0dbbe5, 0x62f7bbe3, 0xc8d68c07, 0x880e950e, 0xf80f25ba, 0x767a264c, 0x9a7ce014, 0x5c8bc9ee, 0x5d9ef7d4, 0xb999acde, 0xb2ec8e13, 0xee68232d, 0x927c5fce, 0xc9e3a85d, 0xac74b56b, 0x42b6e712, 0xcd2898da, 0xfcf11c58, 0xf57075ee, 0x5076e678, 0xd4d66a35, 0x95105ab9, 0x1bb04403, 0xb240b959, 0x7b4e261a, 0x23d129d8, 0xf5e752cd, 0x4ea78f70};
    uint32_t const k[4]= {'t', 'o', 'r', 'a'};
    int n= 66; //n 的绝对值表示 v 的长度，取正表示加密，取负表示解密
    // v 为要加密的数据是两个 32 位无符号整数
    // k 为加密解密密钥，为 4 个 32 位无符号整数，即密钥长度为 128 位
    // printf("Plain: %u %u %u\n",v[0],v[1],v[2]);
    // btea(v, n, k);
    // printf("Encrypted: %u %u %u\n",v[0],v[1],v[2]);
    btea(v, -n, k);
    for (int i = 0; i < n; i++) {
        printf("0x%2x, ", v[i]);
    }
    printf("\n");
    return 0;
}