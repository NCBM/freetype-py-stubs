#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  FreeType high-level python API - Copyright 2011-2015 Nicolas P. Rougier
#  Distributed under the terms of the new BSD license.
#
# -----------------------------------------------------------------------------
'''
Freetype structured types
-------------------------

FT_Library: A handle to a FreeType library instance.

FT_Vector: A simple structure used to store a 2D vector.

FT_BBox: A structure used to hold an outline's bounding box.

FT_Matrix: A simple structure used to store a 2x2 matrix.

FT_UnitVector: A simple structure used to store a 2D vector unit vector.

FT_Bitmap: A structure used to describe a bitmap or pixmap to the raster.

FT_Data: Read-only binary data represented as a pointer and a length.

FT_Generic: Client applications generic data.

FT_Bitmap_Size: Metrics of a bitmap strike.

FT_Charmap: The base charmap structure.

FT_Glyph_Metrics:A structure used to model the metrics of a single glyph.

FT_Outline: This structure is used to describe an outline to the scan-line
            converter.

FT_GlyphSlot: FreeType root glyph slot class structure.

FT_Glyph: The root glyph structure contains a given glyph image plus its
           advance width in 16.16 fixed float format.

FT_Size_Metrics: The size metrics structure gives the metrics of a size object.

FT_Size: FreeType root size class structure.

FT_Face: FreeType root face class structure.

FT_Parameter: A simple structure used to pass more or less generic parameters
              to FT_Open_Face.

FT_Open_Args: A structure used to indicate how to open a new font file or
              stream.

FT_SfntName: A structure used to model an SFNT 'name' table entry.

FT_Stroker: Opaque handler to a path stroker object.

FT_BitmapGlyph: A structure used for bitmap glyph images.
'''
from ctypes import Structure, c_char, c_int, c_short, c_ubyte, c_void_p
from dataclasses import dataclass
from typing import TYPE_CHECKING

from freetype.ft_types import (
    FT_Byte,
    FT_F2Dot14,
    FT_Fixed,
    FT_Generic_Finalizer,
    FT_Int,
    FT_Pos,
    FT_UInt,
)

if TYPE_CHECKING:
    from ctypes import _Pointer


class FT_LibraryRec(Structure):
    '''
    A handle to a FreeType library instance. Each 'library' is completely
    independent from the others; it is the 'root' of a set of objects like
    fonts, faces, sizes, etc.
    '''
    ...


FT_Library = _Pointer[FT_LibraryRec]


@dataclass
class FT_Vector(Structure):
    '''
    A simple structure used to store a 2D vector; coordinates are of the FT_Pos
    type.
    '''
    x: FT_Pos = ...
    """The horizontal coordinate."""
    y: FT_Pos = ...
    """The vertical coordinate."""


@dataclass
class FT_BBox(Structure):
    '''
    A structure used to hold an outline's bounding box, i.e., the coordinates
    of its extrema in the horizontal and vertical directions.

    The bounding box is specified with the coordinates of the lower left and
    the upper right corner. In PostScript, those values are often ',     called
    (llx,lly) and (urx,ury), respectively.

    If 'yMin' is negative, this value gives the glyph's descender. Otherwise,
    the glyph doesn't descend below the baseline. Similarly, if 'ymax' is
    positive, this value gives the glyph's ascender.

    'xMin' gives the horizontal distance from the glyph's origin to the left
    edge of the glyph's bounding box. If 'xMin' is negative, the glyph extends
    to the left of the origin.
    '''
    xMin: FT_Pos = ...
    """The horizontal minimum (left-most)."""
    yMin: FT_Pos = ...
    """The vertical minimum (bottom-most)."""
    xMax: FT_Pos = ...
    """The horizontal maximum (right-most)."""
    yMax: FT_Pos = ...
    """The vertical maximum (top-most)."""


@dataclass
class FT_Matrix(Structure):
    '''
    A simple structure used to store a 2x2 matrix. Coefficients are in 16.16
    fixed float format. The computation performed is:

    x' = x*xx + y*xy
    y' = x*yx + y*yy
    '''
    xx: FT_Fixed = ...
    """Matrix coefficient."""
    xy: FT_Fixed = ...
    """Matrix coefficient."""
    yx: FT_Fixed = ...
    """Matrix coefficient."""
    yy: FT_Fixed = ...
    """Matrix coefficient."""


@dataclass
class FT_UnitVector(Structure):
    '''
    A simple structure used to store a 2D vector unit vector. Uses FT_F2Dot14
    types.
    '''
    x: FT_F2Dot14 = ...
    """The horizontal coordinate."""
    y: FT_F2Dot14 = ...
    """The vertical coordinate."""


@dataclass
class FT_Bitmap(Structure):
    '''
    A structure used to describe a bitmap or pixmap to the raster. Note that we
    now manage pixmaps of various depths through the 'pixel_mode' field.
    '''
    rows: c_int = ...
    """The number of bitmap rows."""
    width: c_int = ...
    """The number of pixels in bitmap row."""
    pitch: c_int = ...
    """
    The pitch's absolute value is the number of bytes taken by one
    bitmap row, including padding. However, the pitch is positive when
    the bitmap has a 'down' flow, and negative when it has an 'up'
    flow. In all cases, the pitch is an offset to add to a bitmap
    pointer in order to go down one row.

    Note that 'padding' means the alignment of a bitmap to a byte
    border, and FreeType functions normally align to the smallest
    possible integer value.

    For the B/W rasterizer, 'pitch' is always an even number.

    To change the pitch of a bitmap (say, to make it a multiple of 4),
    use FT_Bitmap_Convert. Alternatively, you might use callback
    functions to directly render to the application's surface; see the
    file 'example2.py' in the tutorial for a demonstration.
    """
    # declaring buffer as c_char_p confuses ctypes
    buffer: _Pointer[c_ubyte] = ...
    """
    A typeless pointer to the bitmap buffer. This value should be
    aligned on 32-bit boundaries in most cases.
    """
    num_grays: c_short = ...
    """
    This field is only used with FT_PIXEL_MODE_GRAY; it gives the
    number of gray levels used in the bitmap.
    """
    pixel_mode: c_ubyte = ...
    """
    The pixel mode, i.e., how pixel bits are stored. See
    FT_Pixel_Mode for possible values.
    """
    palette_mode: c_char = ...
    """
    This field is intended for paletted pixel modes; it indicates
    how the palette is stored. Not used currently.
    """
    palette: c_void_p = ...
    """
    A typeless pointer to the bitmap palette; this field is intended
    for paletted pixel modes. Not used currently.
    """


@dataclass
class FT_Data(Structure):
    '''
    Read-only binary data represented as a pointer and a length.
    '''
    pointer: _Pointer[FT_Byte] = ...
    """The data."""
    length: FT_Int = ...
    """The length of the data in bytes."""


@dataclass
class FT_Generic(Structure):
    '''
    Client applications often need to associate their own data to a variety of
    FreeType core objects. For example, a text layout API might want to
    associate a glyph cache to a given size object.

    Most FreeType object contains a 'generic' field, of type FT_Generic, which
    usage is left to client applications and font servers.

    It can be used to store a pointer to client-specific data, as well as the
    address of a 'finalizer' function, which will be called by FreeType when
    the object is destroyed (for example, the previous client example would put
    the address of the glyph cache destructor in the 'finalizer' field).

    data: A typeless pointer to any client-specified data. This field is
          completely ignored by the FreeType library.
    finalizer: A pointer to a 'generic finalizer' function, which will be
               called when the object is destroyed. If this field is set to
               NULL, no code will be called.
    '''
    data: c_void_p = ...
    finalizer: FT_Generic_Finalizer = ...
