#ifndef WASM_H_GENERATED_
#define WASM_H_GENERATED_
/* Automically generated by wasm2c */
#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

#include "wasm-rt.h"

#ifndef WASM_RT_MODULE_PREFIX
#define WASM_RT_MODULE_PREFIX
#endif

#define WASM_RT_PASTE_(x, y) x ## y
#define WASM_RT_PASTE(x, y) WASM_RT_PASTE_(x, y)
#define WASM_RT_ADD_PREFIX(x) WASM_RT_PASTE(WASM_RT_MODULE_PREFIX, x)

/* TODO(binji): only use stdint.h types in header */
typedef uint8_t u8;
typedef int8_t s8;
typedef uint16_t u16;
typedef int16_t s16;
typedef uint32_t u32;
typedef int32_t s32;
typedef uint64_t u64;
typedef int64_t s64;
typedef float f32;
typedef double f64;

extern void WASM_RT_ADD_PREFIX(init)(void);

/* import: 'env' 'validate_4' */
extern u32 (*Z_envZ_validate_4Z_ii)(u32);

/* export: 'memory' */
extern wasm_rt_memory_t (*WASM_RT_ADD_PREFIX(Z_memory));
/* export: '__wasm_call_ctors' */
extern void (*WASM_RT_ADD_PREFIX(Z___wasm_call_ctorsZ_vv))(void);
/* export: 'a' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_aZ_iv))(void);
/* export: 'streq' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_streqZ_iii))(u32, u32);
/* export: 'validate_1' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_validate_1Z_ii))(u32);
/* export: 'validate_2' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_validate_2Z_iiiiii))(u32, u32, u32, u32, u32);
/* export: 'validate_3' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_validate_3Z_iiiiii))(u32, u32, u32, u32, u32);
/* export: 'validate_5' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_validate_5Z_iiiiii))(u32, u32, u32, u32, u32);
/* export: 'validate_6' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_validate_6Z_iiiiii))(u32, u32, u32, u32, u32);
/* export: 'guess' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_guessZ_iii))(u32, u32);
/* export: '__indirect_function_table' */
extern wasm_rt_table_t (*WASM_RT_ADD_PREFIX(Z___indirect_function_table));
/* export: '__errno_location' */
extern u32 (*WASM_RT_ADD_PREFIX(Z___errno_locationZ_iv))(void);
/* export: 'fflush' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_fflushZ_ii))(u32);
/* export: 'emscripten_stack_init' */
extern void (*WASM_RT_ADD_PREFIX(Z_emscripten_stack_initZ_vv))(void);
/* export: 'emscripten_stack_get_free' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_emscripten_stack_get_freeZ_iv))(void);
/* export: 'emscripten_stack_get_end' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_emscripten_stack_get_endZ_iv))(void);
/* export: 'stackSave' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_stackSaveZ_iv))(void);
/* export: 'stackRestore' */
extern void (*WASM_RT_ADD_PREFIX(Z_stackRestoreZ_vi))(u32);
/* export: 'stackAlloc' */
extern u32 (*WASM_RT_ADD_PREFIX(Z_stackAllocZ_ii))(u32);
#ifdef __cplusplus
}
#endif

#endif  /* WASM_H_GENERATED_ */
