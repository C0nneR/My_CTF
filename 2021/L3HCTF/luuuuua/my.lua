-- Decompiled using luadec 2.2 rev: 895d923 for Lua 5.3 from https://github.com/viruscamp/luadec
-- Command line: /mnt/c/Users/18502/Downloads/luac 

-- params : ...
-- function num : 0 , upvalues : _ENV
local base64 = {}
if _G.bit32 then
  local extract = (_G.bit32).extract
end
if not extract then
  if _G.bit then
    local shl, shr, band = (_G.bit).lshift, (_G.bit).rshift, (_G.bit).band
    do
      extract = function(v, from, width)
  -- function num : 0_0 , upvalues : band, shr, shl
  return band(shr(v, from), shl(1, width) - 1)
end

    end
  else
    do
      if _G._VERSION == "Lua 5.1" then
        extract = function(v, from, width)
  -- function num : 0_1
  local w = 0
  local flag = 2 ^ from
  for i = 0, width - 1 do
    local flag2 = flag + flag
    if flag <= v % flag2 then
      w = w + 2 ^ i
    end
    flag = flag2
  end
  return w
end

      else
        extract = (load("return function( v, from, width )\n\t\t\treturn ( v >> from ) & ((1 << width) - 1)\n\t\tend"))()
      end
      base64.makeencoder = function(s62, s63, spad)
  -- function num : 0_2 , upvalues : _ENV
  local encoder = {}
  for b64code,char in pairs({"B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", s62 or "+", s63 or "/", spad or "="; [0] = "A"}) do
    encoder[b64code] = char:byte()
  end
  return encoder
end

      base64.makedecoder = function(s62, s63, spad)
  -- function num : 0_3 , upvalues : _ENV, base64
  local decoder = {}
  for b64code,charcode in pairs((base64.makeencoder)(s62, s63, spad)) do
    decoder[charcode] = b64code
  end
  return decoder
end

      local DEFAULT_ENCODER = (base64.makeencoder)()
      local DEFAULT_DECODER = (base64.makedecoder)()
      local char, concat = string.char, table.concat
      base64.encode = function(str, encoder, usecaching)
  -- function num : 0_4 , upvalues : DEFAULT_ENCODER, char, extract, concat
  if not encoder then
    encoder = DEFAULT_ENCODER
  end
  local t, k, n = {}, 1, #str
  local lastn = n % 3
  local cache = {}
  for i = 1, n - lastn, 3 do
    local a, b, c = str:byte(i, i + 2)
    local v = a * 65536 + b * 256 + c
    local s = nil
    if usecaching then
      s = cache[v]
      if not s then
        s = char(encoder[extract(v, 18, 6)], encoder[extract(v, 12, 6)], encoder[extract(v, 6, 6)], encoder[extract(v, 0, 6)])
        cache[v] = s
      end
    else
      s = char(encoder[extract(v, 18, 6)], encoder[extract(v, 12, 6)], encoder[extract(v, 6, 6)], encoder[extract(v, 0, 6)])
    end
    t[k] = s
    k = k + 1
  end
  if lastn == 2 then
    local a, b = str:byte(n - 1, n)
    local v = a * 65536 + b * 256
    t[k] = char(encoder[extract(v, 18, 6)], encoder[extract(v, 12, 6)], encoder[extract(v, 6, 6)], encoder[64])
  else
    do
      do
        if lastn == 1 then
          local v = str:byte(n) * 65536
          t[k] = char(encoder[extract(v, 18, 6)], encoder[extract(v, 12, 6)], encoder[64], encoder[64])
        end
        return concat(t)
      end
    end
  end
end

      base64.decode = function(b64, decoder, usecaching)
  -- function num : 0_5 , upvalues : DEFAULT_DECODER, _ENV, char, extract, concat
  if not decoder then
    decoder = DEFAULT_DECODER
  end
  local pattern = "[^%w%+%/%=]"
  do
    if decoder then
      local s62, s63 = nil, nil
      for charcode,b64code in pairs(decoder) do
        if b64code == 62 then
          s62 = charcode
        else
          if b64code == 63 then
            s63 = charcode
          end
        end
      end
      pattern = ("[^%%w%%%s%%%s%%=]"):format(char(s62), char(s63))
    end
    b64 = b64:gsub(pattern, "")
    if usecaching then
      local cache = {}
    end
    local t, k = {}, 1
    local n = #b64
    local padding = (b64:sub(-2) == "==" and 2) or (b64:sub(-1) == "=" and 1) or 0
    for i = 1, padding > 0 and n - 4 or n, 4 do
      local a, b, c, d = b64:byte(i, i + 3)
      local s = nil
      if usecaching then
        local v0 = a * 16777216 + b * 65536 + c * 256 + d
        s = cache[v0]
        if not s then
          local v = decoder[a] * 262144 + decoder[b] * 4096 + decoder[c] * 64 + decoder[d]
          s = char(extract(v, 16, 8), extract(v, 8, 8), extract(v, 0, 8))
          cache[v0] = s
        end
      else
        do
          do
            do
              local v = decoder[a] * 262144 + decoder[b] * 4096 + decoder[c] * 64 + decoder[d]
              s = char(extract(v, 16, 8), extract(v, 8, 8), extract(v, 0, 8))
              t[k] = s
              k = k + 1
              -- DECOMPILER ERROR at PC143: LeaveBlock: unexpected jumping out DO_STMT

              -- DECOMPILER ERROR at PC143: LeaveBlock: unexpected jumping out DO_STMT

              -- DECOMPILER ERROR at PC143: LeaveBlock: unexpected jumping out IF_ELSE_STMT

              -- DECOMPILER ERROR at PC143: LeaveBlock: unexpected jumping out IF_STMT

            end
          end
        end
      end
    end
    if padding == 1 then
      local a, b, c = b64:byte(n - 3, n - 1)
      local v = decoder[a] * 262144 + decoder[b] * 4096 + decoder[c] * 64
      t[k] = char(extract(v, 16, 8), extract(v, 8, 8))
    else
      do
        if padding == 2 then
          local a, b = b64:byte(n - 3, n - 2)
          local v = decoder[a] * 262144 + decoder[b] * 4096
          t[k] = char(extract(v, 16, 8))
        end
        do
          return concat(t)
        end
      end
    end
  end
end

      local strf = string.format
      local byte, char = string.byte, string.char
      local spack, sunpack = string.pack, string.unpack
      local app, concat = table.insert, table.concat
      local stohex = function(s, ln, sep)
  -- function num : 0_6 , upvalues : strf, byte, concat
  if #s == 0 then
    return ""
  end
  if not ln then
    return s:gsub(".", function(c)
    -- function num : 0_6_0 , upvalues : strf, byte
    return strf("%02x", byte(c))
  end
)
  end
  if not sep then
    sep = ""
  end
  local t = {}
  for i = 1, #s - 1 do
    t[#t + 1] = strf("%02x%s", s:byte(i), i % ln == 0 and "\n" or sep)
  end
  t[#t + 1] = strf("%02x", s:byte(#s))
  return concat(t)
end

      local hextos = function(hs, unsafe)
  -- function num : 0_7 , upvalues : _ENV, char
  local tonumber = tonumber
  if not unsafe then
    hs = (string.gsub)(hs, "%s+", "")
    if (string.find)(hs, "[^0-9A-Za-z]") or #hs % 2 ~= 0 then
      error("invalid hex string")
    end
  end
  return hs:gsub("(%x%x)", function(c)
    -- function num : 0_7_0 , upvalues : char, tonumber
    return char(tonumber(c, 16))
  end
)
end

      local stx = stohex
      local xts = hextos
      local ROUNDS = 64
      local keysetup = function(key)
  -- function num : 0_8 , upvalues : _ENV, sunpack, ROUNDS
  assert(#key == 16)
  local kt = {0, 0, 0, 0}
  kt[1], kt[2], kt[3], kt[4] = sunpack(">I4I4I4I4", key)
  local skt0 = {}
  local skt1 = {}
  local sum, delta = 0, 2654435769
  for i = 1, ROUNDS do
    skt0[i] = sum + kt[(sum & 3) + 1]
    sum = sum + delta & 4294967295
    skt1[i] = (sum) + kt[((sum) >> 11 & 3) + 1]
  end
  do return {skt0 = skt0, skt1 = skt1} end
  -- DECOMPILER ERROR: 1 unprocessed JMP targets
end

      local encrypt_u64 = function(st, bu)
  -- function num : 0_9 , upvalues : ROUNDS
  local skt0, skt1 = st.skt0, st.skt1
  local v0, v1 = bu >> 32, bu & 4294967295
  local sum, delta = 0, 2654435769
  for i = 1, ROUNDS do
    v0 = v0 + ((v1 << 4 ~ v1 >> 5) + v1 ~ skt0[i]) & 4294967295
    v1 = v1 + (((v0) << 4 ~ (v0) >> 5) + (v0) ~ skt1[i]) & 4294967295
  end
  bu = (v0) << 32 | v1
  return bu
end

      enc = function(key, iv, itxt)
  -- function num : 0_10 , upvalues : _ENV, sunpack, keysetup, encrypt_u64, spack, app, concat
  assert(#key == 16, "bad key length")
  assert(#iv == 8, "bad IV length")
  if #itxt == 0 then
    return ""
  end
  local ivu = sunpack("<I8", iv)
  local ot = {}
  local rbn = #itxt
  local ksu, ibu, ob = nil, nil, nil
  local st = keysetup(key)
  for i = 1, #itxt, 8 do
    ksu = encrypt_u64(st, ivu ~ i)
    if rbn < 8 then
      local buffer = (string.sub)(itxt, i) .. (string.rep)("\000", 8 - rbn)
      ibu = sunpack("<I8", buffer)
      ob = (string.sub)(spack("<I8", ibu ~ ksu), 1, rbn)
    else
      ibu = sunpack("<I8", itxt, i)
      ob = spack("<I8", ibu ~ ksu)
      rbn = rbn - 8
    end
    app(ot, ob)
  end
  do return concat(ot) end
  -- DECOMPILER ERROR: 5 unprocessed JMP targets
end

      check_login = function(username, password)
  -- function num : 0_11 , upvalues : base64, enc
  local encoded = (base64.encode)(username)
  if encoded ~= "TDNIX1NlYw==" then
    return false
  end
  username = username .. "!@#$%^&*("
  local x = (base64.encode)(enc(username, "1qazxsw2", password))
  if x == "LKq2dSc30DKJo99bsFgTkQM9dor1gLl2rejdnkw2MBpOud+38vFkCCF13qY=" then
    return true
  end
  return false
end

    end
  end
end

print(enc("L3H_Sec!@#$%^&*(", "1qazxsw2", ",\xaa\xb6u'7\xd02\x89\xa3\xdf[\xb0X\x13\x91\x03=v\x8a\xf5\x80\xb9v\xad\xe8\xdd\x9eL60\x1aN\xb9\xdf\xb7\xf2\xf1d\x08!u\xde\xa6"))