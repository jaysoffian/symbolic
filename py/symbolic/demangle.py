from symbolic._lowlevel import ffi, lib
from symbolic.utils import encode_str, decode_str, rustcall


__all__ = ['demangle_symbol']


def demangle_symbol(symbol, lang=None, no_args=False):
    """Demangles a symbol."""
    func = lib.symbolic_demangle_no_args if no_args else lib.symbolic_demangle
    lang_str = encode_str(lang) if lang else ffi.NULL
    return decode_str(rustcall(func, encode_str(symbol), lang_str), free=True)
