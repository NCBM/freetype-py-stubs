# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  FreeType high-level python API - Copyright 2011-2015 Nicolas P. Rougier
#  Distributed under the terms of the new BSD license.
#
# -----------------------------------------------------------------------------
"""
An enumeration type used to describe the format of a given glyph image. Note
that this version of FreeType only supports two image formats, even though
future font drivers will be able to register their own format.

FT_GLYPH_FORMAT_NONE

  The value 0 is reserved.

FT_GLYPH_FORMAT_COMPOSITE

  The glyph image is a composite of several other images. This format is only
  used with FT_LOAD_NO_RECURSE, and is used to report compound glyphs (like
  accented characters).

FT_GLYPH_FORMAT_BITMAP

  The glyph image is a bitmap, and can be described as an FT_Bitmap. You
  generally need to access the 'bitmap' field of the FT_GlyphSlotRec structure
  to read it.

FT_GLYPH_FORMAT_OUTLINE

  The glyph image is a vectorial outline made of line segments and Bezier arcs;
  it can be described as an FT_Outline; you generally want to access the
  'outline' field of the FT_GlyphSlotRec structure to read it.

FT_GLYPH_FORMAT_PLOTTER

  The glyph image is a vectorial path with no inside and outside contours. Some
  Type 1 fonts, like those in the Hershey family, contain glyphs in this
  format. These are described as FT_Outline, but FreeType isn't currently
  capable of rendering them correctly.

FT_GLYPH_FORMAT_SVG

  [Since 2.12] The glyph is represented by an SVG document in the 'SVG~' table.
"""

_FtImageTag = int

def _FT_IMAGE_TAG(a: str, b: str, c: str, d: str) -> _FtImageTag:
    ...

FT_GLYPH_FORMATS: dict[str, _FtImageTag]

ft_glyph_format_none      = FT_GLYPH_FORMAT_NONE = _FT_IMAGE_TAG( '\0','\0','\0','\0' )
ft_glyph_format_composite = FT_GLYPH_FORMAT_COMPOSITE = _FT_IMAGE_TAG( 'c','o','m','p' )
ft_glyph_format_bitmap    = FT_GLYPH_FORMAT_BITMAP = _FT_IMAGE_TAG( 'b','i','t','s' )
ft_glyph_format_outline   = FT_GLYPH_FORMAT_OUTLINE = _FT_IMAGE_TAG( 'o','u','t','l' )
ft_glyph_format_plotter   = FT_GLYPH_FORMAT_PLOTTER = _FT_IMAGE_TAG( 'p','l','o','t' )
ft_glyph_format_svg       = FT_GLYPH_FORMAT_SVG = _FT_IMAGE_TAG( 'S','V','G',' ' )
