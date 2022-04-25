section .text
bits 32
label_0:
    sub esp, 84;
label_5:
    push 10;
label_10:
    push 123456789;
label_15:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_16:
    push 11;
label_21:
    push 987654321;
label_26:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_27:
    push 18;
label_32:
    push 0;
label_37:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_38:
    push 19;
label_43:
    push 0;
label_48:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_49:
    push 19;
label_54:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_55:
    push 10;
label_60:
    pop eax;
    pop ebx;
    push eax;
    push ebx;
label_61:
    pop eax;
    pop ebx;
    sub eax, ebx;
    push eax;
label_62:
    mov eax, [esp];
    shr eax, 31;
    mov [esp], eax;
label_63:
    xor ebx,ebx;
    mov eax, [esp];
    test eax, eax;
    sete bl;
    mov [esp], ebx;
label_64:
    pop eax;
    cmp eax, 0;
    jnz label_137;
label_69:
    push 19;
label_74:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_75:
    push 0;
label_80:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_81:
    push 19;
label_86:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_87:
    push 0;
label_92:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_93:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_94:
    push 19;
label_99:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_100:
    push 1;
label_105:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_106:
    push 16843009;
label_111:
    pop eax;
    pop ebx;
    imul eax, ebx;
    push eax;
label_112:
    pop eax;
    pop ebx;
    xor eax, ebx;
    push eax;
label_113:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_114:
    push 19;
label_119:
    push 19;
label_124:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_125:
    push 1;
label_130:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_131:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_132:
    jmp label_49;
label_137:
    push 0;
label_142:
    push 14;
label_147:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_148:
    push 18764;
label_153:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_154:
    push 1;
label_159:
    push 14;
label_164:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_165:
    push 28534;
label_170:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_171:
    push 2;
label_176:
    push 14;
label_181:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_182:
    push 25888;
label_187:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_188:
    push 3;
label_193:
    push 14;
label_198:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_199:
    push 17237;
label_204:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_205:
    push 19;
label_210:
    push 0;
label_215:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_216:
    push 19;
label_221:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_222:
    push 10;
label_227:
    pop eax;
    pop ebx;
    push eax;
    push ebx;
label_228:
    pop eax;
    pop ebx;
    sub eax, ebx;
    push eax;
label_229:
    mov eax, [esp];
    shr eax, 31;
    mov [esp], eax;
label_230:
    xor ebx,ebx;
    mov eax, [esp];
    test eax, eax;
    sete bl;
    mov [esp], ebx;
label_231:
    pop eax;
    cmp eax, 0;
    jnz label_578;
label_236:
    push 20;
label_241:
    push 0;
label_246:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_247:
    push 20;
label_252:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_253:
    push 20;
label_258:
    pop eax;
    pop ebx;
    push eax;
    push ebx;
label_259:
    pop eax;
    pop ebx;
    sub eax, ebx;
    push eax;
label_260:
    mov eax, [esp];
    shr eax, 31;
    mov [esp], eax;
label_261:
    xor ebx,ebx;
    mov eax, [esp];
    test eax, eax;
    sete bl;
    mov [esp], ebx;
label_262:
    pop eax;
    cmp eax, 0;
    jnz label_555;
label_267:
    push 12;
label_272:
    push 19;
label_277:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_278:
    push 0;
label_283:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_284:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_285:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_286:
    push 13;
label_291:
    push 19;
label_296:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_297:
    push 1;
label_302:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_303:
    push 0;
label_308:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_309:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_310:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_311:
    push 12;
label_316:
    push 12;
label_321:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_322:
    push 13;
label_327:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_328:
    push 16;
label_333:
    pop eax;
    pop ebx;
    imul eax, ebx;
    push eax;
label_334:
    push 13;
label_339:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_340:
    push 32;
label_345:
    pop eax;
    pop ebx;
    push eax;
    push ebx;
label_346:
    xor edx, edx;
    pop eax;
    pop ebx;
    idiv ebx;
    push eax;    
label_347:
    pop eax;
    pop ebx;
    xor eax, ebx;
    push eax;
label_348:
    push 13;
label_353:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_354:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_355:
    push 11;
label_360:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_361:
    push 11;
label_366:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_367:
    push 3;
label_372:
    pop eax;
    pop ebx;
    and eax, ebx;
    push eax;
label_373:
    push 14;
label_378:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_379:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_380:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_381:
    pop eax;
    pop ebx;
    xor eax, ebx;
    push eax;
label_382:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_383:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_384:
    push 11;
label_389:
    push 11;
label_394:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_395:
    push 10;
label_400:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_401:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_402:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_403:
    push 13;
label_408:
    push 13;
label_413:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_414:
    push 12;
label_419:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_420:
    push 16;
label_425:
    pop eax;
    pop ebx;
    imul eax, ebx;
    push eax;
label_426:
    push 12;
label_431:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_432:
    push 32;
label_437:
    pop eax;
    pop ebx;
    push eax;
    push ebx;
label_438:
    xor edx, edx;
    pop eax;
    pop ebx;
    idiv ebx;
    push eax;    
label_439:
    pop eax;
    pop ebx;
    xor eax, ebx;
    push eax;
label_440:
    push 12;
label_445:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_446:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_447:
    push 11;
label_452:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_453:
    push 11;
label_458:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_459:
    push 2048;
label_464:
    pop eax;
    pop ebx;
    push eax;
    push ebx;
label_465:
    xor edx, edx;
    pop eax;
    pop ebx;
    idiv ebx;
    push eax;    
label_466:
    push 3;
label_471:
    pop eax;
    pop ebx;
    and eax, ebx;
    push eax;
label_472:
    push 14;
label_477:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_478:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_479:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_480:
    pop eax;
    pop ebx;
    xor eax, ebx;
    push eax;
label_481:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_482:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_483:
    push 19;
label_488:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_489:
    push 0;
label_494:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_495:
    push 12;
label_500:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_501:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_502:
    push 19;
label_507:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_508:
    push 1;
label_513:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_514:
    push 0;
label_519:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_520:
    push 13;
label_525:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_526:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_527:
    mov eax, 1;
    retn;
label_532:
    push 20;
label_537:
    push 20;
label_542:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_543:
    push 1;
label_548:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_549:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_550:
    jmp label_247;
label_555:
    push 19;
label_560:
    push 19;
label_565:
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
label_566:
    push 2;
label_571:
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
label_572:
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
label_573:
    jmp label_216;
label_578:
    mov eax, 0;
    retn;
