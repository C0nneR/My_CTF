<html>
    <script>
        var _0x71a0fe = _0x5b15;
        function _0x54f3() {
            var _0x695892 = ['getElementById', '4787853SBLwXC', 'value', 'success!', 'match', 'filter', '152223ILKqKk', 'reload', '([0-9a-f]{4,12})', '7454488gQLWNt', '3771630sdrcXm', 'location', 'log', '6VNjKDn', '6371240IVxYcx', 'matchAll', '4948280PfzqUs', '42cXdJpF', 'flag_input', 'length', '1829548EQHzrX', 'push', 'failed!', 'addListener', 'next'];
            _0x54f3 = function() {
                return _0x695892;
            }
            ;
            return _0x54f3();
        }
        (function(_0x3c6563, _0x328c1b) {
            var _0x2e3bf5 = _0x5b15
              , _0x588dab = _0x3c6563();
            while (!![]) {
                try {
                    var _0x27dd68 = parseInt(_0x2e3bf5(0x100)) / 0x1 + parseInt(_0x2e3bf5(0xfd)) / 0x2 * (-parseInt(_0x2e3bf5(0x10b)) / 0x3) + parseInt(_0x2e3bf5(0x10e)) / 0x4 + parseInt(_0x2e3bf5(0xfa)) / 0x5 * (-parseInt(_0x2e3bf5(0xf9)) / 0x6) + parseInt(_0x2e3bf5(0x106)) / 0x7 + -parseInt(_0x2e3bf5(0xfc)) / 0x8 + -parseInt(_0x2e3bf5(0x10f)) / 0x9;
                    if (_0x27dd68 === _0x328c1b)
                        break;
                    else
                        _0x588dab['push'](_0x588dab['shift']());
                } catch (_0xd6f271) {
                    _0x588dab['push'](_0x588dab['shift']());
                }
            }
        }(_0x54f3, 0xf4137));
        var delta = 0x1
          , check_result = new Uint32Array(0x6);
        check_result[0x0] = -0x3dec3227,
        check_result[0x1] = 0x79f40242,
        check_result[0x2] = 0x325d0365,
        check_result[0x3] = 0x6561df78,
        check_result[0x4] = 0x5747f7c8,
        check_result[0x5] = -0x26c12bcb,
        function() {
            var _0xa7cfb9 = []
              , _0x2d5744 = 0x32
              , _0x428313 = ![]
              , _0x35eee4 = 0x0
              , _0x33d074 = 0x0
              , _0x394f2f = 0x0;
            setInterval(_0x307ff0, 0x1),
            setInterval(_0x87360, 0x1),
            setInterval(_0x430300, 0x1);
            return {
                'addListener': function(_0x42fda0) {
                    var _0x248679 = _0x5b15;
                    _0xa7cfb9.push(_0x42fda0);
                },
                'cancleListenr': function(_0x3a07da) {
                    var _0x500ecf = _0x5b15;
                    _0xa7cfb9 = _0xa7cfb9['filter'](function(_0x57e814) {
                        return _0x57e814 !== _0x3a07da;
                    });
                }
            };
            function _0x307ff0() {
                _0x35eee4 = new Date();
                debugger ;
            }
            function _0x87360() {
                _0x33d074 = new Date(),
                _0x33d074 - _0x35eee4 > _0x2d5744 && (delta = 0xa);
            }
            function _0x430300() {
                _0x394f2f = new Date(),
                _0x394f2f - _0x35eee4 > _0x2d5744 && (check_result[0x3] = 0x0);
            }
        }()['addListener'](function() {
            var _0x150596 = _0x71a0fe;
            window['location']['reload']();
        });
        function encryptBlock(input, keys, round, input_index) {
            var keys = keys, v0 = input[input_index % input['length']], v1 = input[(input_index + 0x1) % input['length']], sum = 0x0, i, key_0 = keys[0x0], key_1 = keys[0x1], key_2 = keys[0x2], key_3 = keys[0x3];
            for (i = 0x0; i < round; i++) {
                sum = sum + delta | 0x0,
                v0 = v0 + ((v1 << 0x4) + key_0 ^ v1 + sum ^ (v1 >>> 0x5) + key_1) | 0x0,
                v1 = v1 + ((v0 << 0x4) + key_2 ^ v0 + sum ^ (v0 >>> 0x5) + key_3) | 0x0;
            }
            input[input_index % input['length']] = v0,
            input[(input_index + 0x1) % input['length']] = v1;
        }
        function _0x5b15(_0x4f2f0e, _0x17f36f) {
            var _0x54f38d = _0x54f3();
            return _0x5b15 = function(_0x5b1536, _0x43759a) {
                _0x5b1536 = _0x5b1536 - 0xf9;
                var _0x359573 = _0x54f38d[_0x5b1536];
                return _0x359573;
            }
            ,
            _0x5b15(_0x4f2f0e, _0x17f36f);
        }

        function check() {
            var _0x2b6df1 = _0x71a0fe
              , flag_input = document.getElementById('flag_input')['value'];
            if (flag_input['length'] == 0x2a && flag_input.match('^flag{[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}}$')) {
                var input = []
                  , _0x1523bd = flag_input.matchAll('([0-9a-f]{4,12})')
                  , _0x1e4dbc = _0x1523bd['next']();
                while (_0x1e4dbc['value']) {
                    if (parseInt(_0x1e4dbc['value'], 0x10) > 0xffffffff) {
                        alert('failed!');
                        return;
                    }
                    input.push(parseInt(_0x1e4dbc['value'], 0x10)),
                    _0x1e4dbc = _0x1523bd['next']();
                }
                input['length'] % 0x2 == 0x1 && input.push(0xdeadbeef);
                var i = 0x0;
                while (i < input['length']) {
                    var keys = [input[(0x2 + i) % input['length']], input[(0x3 + i) % input['length']], input[(0x4 + i) % input['length']], input[(0x5 + i) % input['length']]];
                    encryptBlock(input, keys, 0x22, i),
                    i += 0x1;
                }
                var encrypted_input = new Uint32Array(input['length']);
                i = 0x0;
                while (i < input['length']) {
                    encrypted_input[i] = input[i],
                    i += 0x1;
                }
                i = 0x0;
                while (i < check_result['length']) {
                    if (check_result[i] != encrypted_input[i]) {
                        alert('failed!');
                        return;
                    }
                    i += 0x1;
                }
                alert('success!');
                return;
            } else
                console[_0x2b6df1(0x111)]('format\x20error');
        }
    </script>
    <input type="text" id='flag_input'>
    <button onclick="check()">check!</button>
</html>