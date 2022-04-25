.686p
.mmx
.model flat
.stack 100h
.code
_main proc
    pushad
    cld
    push 726774Ch
    xor edx, edx
    ASSUME fs:NOTHING
    mov edx, fs:[edx+30h]
    ASSUME fs:ERROR
    mov edx, [edx+0Ch]
    mov edx, [edx+14h]

FOUR:
    mov esi, [edx+28h]
    movzx ecx, word ptr [edx+26h]
    xor edi, edi

TWO:
    xor eax, eax
    lodsb
    cmp al, 61h
    jl ONE
    sub al, 20h

ONE:
    ror edi, 0Dh
    add edi, eax
    loop TWO
    push edx
    push edi
    mov edx, [edx+10h]
    mov eax, [edx+3Ch]
    add eax, edx
    mov eax, [eax+78h]
    test eax, eax
    jz THREE
    add eax, edx
    push eax
    mov ecx, [eax+18h]
    mov ebx, [eax+20h]
    add ebx, edx

SEVEN:
    cmp ecx, 0
    jz FIVE
    dec ecx
    mov esi, [ebx+ecx*4]
    add esi,edx
    xor edi, edi

SIX:
    xor eax, eax
    lodsb
    ror edi, 0Dh
    add edi, eax
    cmp al, ah
    jnz six
    add edi, [esp+4]
    cmp edi, [esp+0Ch]
    jnz SEVEN
    xor edi, edi
    xor ecx, ecx
    add edx, 50h

EIGHT:
    movzx eax, byte ptr [edx+ecx]
    ror edi, 0Dh
    add edi, eax
    inc ecx
    cmp ecx, 0Eh
    jnz EIGHT
    ror edi, 0Dh
    push edi
    xor edi, edi
    xor ecx, ecx
    mov edx, [esp+3Ch]

NINE:
    push edx
    movzx ebx, byte ptr [esi+ecx]
    mov eax, 66666667h
    imul ebx
    sar edx, 1
    mov eax, edx
    shr eax, 1Fh
    add eax, edx
    lea eax, dword ptr [eax+eax*4]
    sub ebx, eax
    pop edx
    movzx eax, byte ptr [edx+ecx]
    sub eax, ebx
    ror edi, 0Dh
    add edi, eax
    inc ecx
    cmp ecx, 0Eh
    jnz NINE
    ror edi, 0Dh
    cmp edi, [esp]
    jz RIGHT
    push 7325h
    mov eax, esp
    push 6f6eh
    push esp
    push eax
    mov ebx, [esp+48h]
    call ebx
    jmp FINAL

RIGHT:
    push 7325h
    mov eax, esp
    push 736579h
    push esp
    push eax
    mov ebx, [esp+48h]
    call ebx

FINAL:
    pop eax
    pop eax
    pop eax
    pop eax
    pop eax
    pop eax
    pop eax
    pop eax
    pop eax
    popad
    ret

FIVE:
    pop eax

THREE:
    pop edi
    pop edx
    mov edx, [edx]
    jmp FOUR
    
_main endp
end _main