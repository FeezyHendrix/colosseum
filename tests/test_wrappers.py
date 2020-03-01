from collections import OrderedDict
from itertools import permutations
from unittest import TestCase

from colosseum.units import px
from colosseum.wrappers import (Border, BorderBottom, BorderLeft, BorderRight,
                                BorderSpacing, BorderTop, Outline, Quotes,
                                Shorthand)


class BorderSpacingTests(TestCase):

    def test_valid_1_arg_string(self):
        border_spacing = BorderSpacing('1')
        self.assertEqual(border_spacing.horizontal, '1')
        self.assertEqual(border_spacing.vertical, '1')
        self.assertEqual(str(border_spacing), '1')
        self.assertEqual(repr(border_spacing), "BorderSpacing('1')")

    def test_valid_1_arg_int(self):
        border_spacing = BorderSpacing(1)
        self.assertEqual(border_spacing.horizontal, 1)
        self.assertEqual(border_spacing.vertical, 1)
        self.assertEqual(str(border_spacing), '1')
        self.assertEqual(repr(border_spacing), "BorderSpacing(1)")

    def test_valid_1_arg_px(self):
        border_spacing = BorderSpacing(1 * px)
        self.assertEqual(border_spacing.horizontal, 1 * px)
        self.assertEqual(border_spacing.vertical, 1 * px)
        self.assertEqual(str(border_spacing), '1px')
        self.assertEqual(repr(border_spacing), "BorderSpacing(1px)")

    def test_valid_2_arg_str(self):
        border_spacing = BorderSpacing('1', '2')
        self.assertEqual(border_spacing.horizontal, '1')
        self.assertEqual(border_spacing.vertical, '2')
        self.assertEqual(str(border_spacing), '1 2')
        self.assertEqual(repr(border_spacing), "BorderSpacing('1', '2')")

    def test_valid_2_arg_int(self):
        border_spacing = BorderSpacing(1, 2)
        self.assertEqual(border_spacing.horizontal, 1)
        self.assertEqual(border_spacing.vertical, 2)
        self.assertEqual(str(border_spacing), '1 2')
        self.assertEqual(repr(border_spacing), 'BorderSpacing(1, 2)')

    def test_valid_2_arg_px(self):
        border_spacing = BorderSpacing(1 * px, 2 * px)
        self.assertEqual(border_spacing.horizontal, 1 * px)
        self.assertEqual(border_spacing.vertical, 2 * px)
        self.assertEqual(str(border_spacing), '1px 2px')
        self.assertEqual(repr(border_spacing), 'BorderSpacing(1px, 2px)')

    def test_invalid_arg_number(self):
        with self.assertRaises(TypeError):
            BorderSpacing(1, 2, 3)


class QuotesTests(TestCase):

    # Valid cases
    def test_quotes_valid_1_pair(self):
        quotes = Quotes([('<', '>')])

        self.assertEqual(quotes.opening(level=0), '<')
        self.assertEqual(quotes.closing(level=0), '>')
        self.assertEqual(len(quotes), 1)
        self.assertEqual(str(quotes), "'<' '>'")
        self.assertEqual(repr(quotes), "Quotes([('<', '>')])")

    def test_quotes_valid_2_pairs(self):
        quotes = Quotes([('<', '>'), ('{', '}')])

        self.assertEqual(quotes.opening(level=0), '<')
        self.assertEqual(quotes.closing(level=0), '>')
        self.assertEqual(quotes.opening(level=1), '{')
        self.assertEqual(quotes.closing(level=1), '}')
        self.assertEqual(len(quotes), 2)
        self.assertEqual(str(quotes), "'<' '>' '{' '}'")
        self.assertEqual(repr(quotes), "Quotes([('<', '>'), ('{', '}')])")

    # Invalid cases
    def test_quotes_invalid_1_pair_level(self):
        quotes = Quotes([('<', '>')])

        with self.assertRaises(IndexError):
            quotes.opening(level=1)

        with self.assertRaises(IndexError):
            quotes.closing(level=1)


class TestShorthand(TestCase):

    def test_shorthand_invalid_empty(self):
        with self.assertRaises(ValueError):
            Shorthand()


class TestShorthandOutline(TestCase):

    def test_shorthand_outline_valid_empty(self):
        outline = Outline()
        self.assertEqual(str(outline), '')
        self.assertEqual(repr(outline), 'Outline()')

    def test_shorthand_outline_valid_1_kwargs(self):
        for property_name in ['outline_color', 'outline_style', 'outline_width']:
            outline = Outline(**{property_name: 1})
            self.assertEqual(str(outline), '1')
            self.assertEqual(getattr(outline, property_name), 1)

    def test_shorthand_outline_valid_2_kwargs(self):
        perms = permutations(['outline_color', 'outline_style', 'outline_width'], 2)
        for (prop_1, prop_2) in perms:
            kwargs = {prop_1: 1, prop_2: 2}
            outline = Outline(**kwargs)
            self.assertEqual(str(outline), ' '.join(str(v[1]) for v in sorted(kwargs.items())))

    def test_shorthand_outline_valid_3_kwargs(self):
        perms = permutations(['outline_color', 'outline_style', 'outline_width'])
        for (prop_1, prop_2, prop_3) in perms:
            kwargs = {prop_1: 1, prop_2: 2, prop_3: 3}
            outline = Outline(**kwargs)
            self.assertEqual(str(outline), ' '.join(str(v[1]) for v in sorted(kwargs.items())))

    def test_shorthand_outline_valid_get_values(self):
        perms = permutations(['outline_color', 'outline_style', 'outline_width'])
        for (prop_1, prop_2, prop_3) in perms:
            kwargs = {prop_1: 1, prop_2: 2, prop_3: 3}
            outline = Outline(**kwargs)
            self.assertEqual(getattr(outline, prop_1), kwargs[prop_1])
            self.assertEqual(getattr(outline, prop_2), kwargs[prop_2])
            self.assertEqual(getattr(outline, prop_3), kwargs[prop_3])

    def test_shorthand_outline_valid_set_values(self):
        perms = permutations(['outline_color', 'outline_style', 'outline_width'])
        for (prop_1, prop_2, prop_3) in perms:
            kwargs = {prop_1: 1, prop_2: 2, prop_3: 3}
            outline = Outline(**kwargs)
            self.assertEqual(getattr(outline, prop_1), kwargs[prop_1])
            self.assertEqual(getattr(outline, prop_2), kwargs[prop_2])
            self.assertEqual(getattr(outline, prop_3), kwargs[prop_3])

    def test_shorthand_outline_equality(self):
        perms = permutations(['outline_color', 'outline_style', 'outline_width'])
        for (prop_1, prop_2, prop_3) in perms:
            kwargs = {prop_1: 1, prop_2: 2, prop_3: 3}
            outline1 = Outline(**kwargs)
            outline2 = Outline(**kwargs)
            self.assertEqual(outline1, outline2)

    def test_shorthand_outline_valid_to_dict(self):
        expected_output = ['outline_color', 'outline_style', 'outline_width']
        perms = permutations(expected_output)
        for (prop_1, prop_2, prop_3) in perms:
            kwargs = {prop_1: 1, prop_2: 2, prop_3: 3}
            outline = Outline(**kwargs)
            self.assertEqual(outline.to_dict(), kwargs)

    # Invalid cases
    def test_shorthand_outline_invalid_kwargs(self):
        with self.assertRaises(ValueError):
            Outline(foobar='foobar')


class TestShorthandBorder(TestCase):

    def test_shorthand_boder_valid_empty(self):
        for wrapper_class in [Border, BorderBottom, BorderLeft, BorderRight, BorderTop]:
            wrapper = wrapper_class()
            self.assertEqual(str(wrapper), '')
            self.assertEqual(repr(wrapper), wrapper_class.__name__ + '()')

    def test_shorthand_outline_valid_1_kwargs(self):
        for direction, wrapper_class in {'': Border,
                                         'bottom_': BorderBottom,
                                         'left_': BorderLeft,
                                         'right_': BorderRight,
                                         'top_': BorderTop}.items():

            for property_name in ['border_{direction}color'.format(direction=direction),
                                  'border_{direction}style'.format(direction=direction),
                                  'border_{direction}width'.format(direction=direction)]:

                wrapper = wrapper_class(**{property_name: 1})
                self.assertEqual(str(wrapper), '1')
                self.assertEqual(getattr(wrapper, property_name), 1)

    def test_shorthand_outline_valid_2_kwargs(self):
        for direction, wrapper_class in {'': Border,
                                         'bottom_': BorderBottom,
                                         'left_': BorderLeft,
                                         'right_': BorderRight,
                                         'top_': BorderTop}.items():

            perms = permutations(['border_{direction}color'.format(direction=direction),
                                  'border_{direction}style'.format(direction=direction),
                                  'border_{direction}width'.format(direction=direction)], 2)

            for (prop_1, prop_2) in perms:
                kwargs = OrderedDict()

                # This is to guarantee the proper order
                for property_name in wrapper_class.VALID_KEYS:
                    if prop_1 == property_name:
                        kwargs[prop_1] = 1

                    elif prop_2 == property_name:
                        kwargs[prop_2] = 2

                wrapper = wrapper_class(**kwargs)
                self.assertEqual(str(wrapper), ' '.join(str(v[1]) for v in kwargs.items()))

    def test_shorthand_outline_valid_3_kwargs(self):
        for direction, wrapper_class in {'': Border,
                                         'bottom_': BorderBottom,
                                         'left_': BorderLeft,
                                         'right_': BorderRight,
                                         'top_': BorderTop}.items():

            perms = permutations(['border_{direction}color'.format(direction=direction),
                                  'border_{direction}style'.format(direction=direction),
                                  'border_{direction}width'.format(direction=direction)])

            for (prop_1, prop_2, prop_3) in perms:
                kwargs = OrderedDict()

                # This is to guarantee the proper order
                for idx, property_name in enumerate(wrapper_class.VALID_KEYS):
                    kwargs[property_name] = idx + 1

                wrapper = wrapper_class(**kwargs)
                self.assertEqual(str(wrapper), ' '.join(str(v[1]) for v in kwargs.items()))

    def test_shorthand_outline_valid_get_values(self):
        for direction, wrapper_class in {'': Border,
                                         'bottom_': BorderBottom,
                                         'left_': BorderLeft,
                                         'right_': BorderRight,
                                         'top_': BorderTop}.items():

            perms = permutations(['border_{direction}color'.format(direction=direction),
                                  'border_{direction}style'.format(direction=direction),
                                  'border_{direction}width'.format(direction=direction)])

            for (prop_1, prop_2, prop_3) in perms:
                kwargs = OrderedDict()

                # This is to guarantee the proper order
                for idx, property_name in enumerate(wrapper_class.VALID_KEYS):
                    kwargs[property_name] = idx + 1

                wrapper = wrapper_class(**kwargs)
                self.assertEqual(getattr(wrapper, prop_1), kwargs[prop_1])
                self.assertEqual(getattr(wrapper, prop_2), kwargs[prop_2])
                self.assertEqual(getattr(wrapper, prop_3), kwargs[prop_3])

    def test_shorthand_outline_valid_set_values(self):
        for direction, wrapper_class in {'': Border,
                                         'bottom_': BorderBottom,
                                         'left_': BorderLeft,
                                         'right_': BorderRight,
                                         'top_': BorderTop}.items():

            perms = permutations(['border_{direction}color'.format(direction=direction),
                                  'border_{direction}style'.format(direction=direction),
                                  'border_{direction}width'.format(direction=direction)])

            for (prop_1, prop_2, prop_3) in perms:
                kwargs = OrderedDict()

                # This is to guarantee the proper order
                for idx, property_name in enumerate(wrapper_class.VALID_KEYS):
                    kwargs[property_name] = idx + 1

                wrapper = wrapper_class(**kwargs)
                self.assertEqual(getattr(wrapper, prop_1), kwargs[prop_1])
                self.assertEqual(getattr(wrapper, prop_2), kwargs[prop_2])
                self.assertEqual(getattr(wrapper, prop_3), kwargs[prop_3])

    def test_shorthand_outline_equality(self):
        for direction, wrapper_class in {'': Border,
                                         'bottom_': BorderBottom,
                                         'left_': BorderLeft,
                                         'right_': BorderRight,
                                         'top_': BorderTop}.items():

            perms = permutations(['border_{direction}color'.format(direction=direction),
                                  'border_{direction}style'.format(direction=direction),
                                  'border_{direction}width'.format(direction=direction)])

            for (prop_1, prop_2, prop_3) in perms:
                kwargs = OrderedDict()

                # This is to guarantee the proper order
                for idx, property_name in enumerate(wrapper_class.VALID_KEYS):
                    kwargs[property_name] = idx + 1

                wrapper1 = wrapper_class(**kwargs)
                wrapper2 = wrapper_class(**kwargs)
                self.assertEqual(wrapper1, wrapper2)

    def test_shorthand_outline_valid_to_dict(self):
        for direction, wrapper_class in {'': Border,
                                         'bottom_': BorderBottom,
                                         'left_': BorderLeft,
                                         'right_': BorderRight,
                                         'top_': BorderTop}.items():

            perms = permutations(['border_{direction}color'.format(direction=direction),
                                  'border_{direction}style'.format(direction=direction),
                                  'border_{direction}width'.format(direction=direction)])

            for (prop_1, prop_2, prop_3) in perms:
                kwargs = OrderedDict()

                # This is to guarantee the proper order
                for idx, property_name in enumerate(wrapper_class.VALID_KEYS):
                    kwargs[property_name] = idx + 1

                wrapper = wrapper_class(**kwargs)
                self.assertEqual(wrapper.to_dict(), kwargs)

    # Invalid cases
    def test_shorthand_outline_invalid_kwargs(self):
        for wrapper_class in [Border, BorderBottom, BorderLeft, BorderRight, BorderTop]:
            with self.assertRaises(ValueError):
                wrapper_class(foobar='foobar')
