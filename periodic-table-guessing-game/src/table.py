from elements import Element


class Table(Element):
    def __init__(self):
        self.table = (
            # 1st period
            Element(1, 'Hydrogen', 1, 1, 'H'),
            Element(2, 'Helium', 1, 18, 'He'),
            # 2nd period
            Element(3, 'Lithium', 2, 1, 'Li'),
            Element(4, 'Beryllium', 2, 2, 'Li'),
            Element(5, 'Boron', 2, 13, 'B'),
            Element(6, 'Carbon', 2, 14, 'C'),
            Element(7, 'Nitrogen', 2, 15, 'N'),
            Element(8, 'Oxygen', 2, 16, 'O'),
            Element(9, 'Fluorine', 2, 17, 'F'),
            Element(10, 'Neon', 2, 18, 'Ne'),
            # 3rd period
            Element(11, 'Sodium', 3, 1, 'Na'),
            Element(12, 'Magnesium', 3, 2, 'Mg'),
            Element(13, 'Aluminium', 3, 13, 'Al'),
            Element(14, 'Silicon', 3, 14, 'Si'),
            Element(15, 'Phosphorus', 3, 15, 'P'),
            Element(16, 'Sulfur', 3, 16, 's'),
            Element(17, 'Chlorine', 3, 17, 'Cl'),
            Element(18, 'Argon', 3, 18, 'Ar'),
            # 4th period
            Element(19, 'Potassium', 4, 1, 'K'),
            Element(20, 'Calcium', 4, 2, 'Ca'),
            Element(21, 'Scandium', 4, 3, 'Sc'),
            Element(22, 'Titanium', 4, 4, 'Ti'),
            Element(23, 'Vanadium', 4, 5, 'V'),
            Element(24, 'Chromium', 4, 6, 'Cr'),
            Element(25, 'Manganese', 4, 7, 'Mn'),
            Element(26, 'Iron', 4, 8, 'Fe'),
            Element(27, 'Cobalt', 4, 9, 'Co'),
            Element(28, 'Nickel', 4, 10, 'Ni'),
            Element(29, 'Copper', 4, 11, 'Cu'),
            Element(30, 'Zinc', 4, 12, 'Zn'),
            Element(31, 'Gallium', 4, 13, 'Ga'),
            Element(32, 'Germanium', 4, 14, 'Ge'),
            Element(33, 'Arsenic', 4, 15, 'As'),
            Element(34, 'Selenium', 4, 16, 'Se'),
            Element(35, 'Bromine', 4, 17, 'Br'),
            Element(36, 'Krypton', 4, 18, 'Kr'),
            # 5th period
            Element(37, 'Rubidium', 5, 1, 'Rb'),
            Element(38, 'Strontium', 5, 2, 'Sr'),
            Element(39, 'Scandium', 5, 3, 'Sc'),
            Element(40, 'Zirconium', 5, 4, 'Zr'),
            Element(41, 'Niobium', 5, 5, 'Nb'),
            Element(42, 'Molybdenur', 5, 6, 'Mo'),
            Element(43, 'Technetium', 5, 7, 'Tc'),
            Element(44, 'Ruthenium', 5, 8, 'Ru'),
            Element(45, 'Rhodium', 5, 9, 'Rh'),
            Element(46, 'Palladium', 5, 10, 'Pd'),
            Element(47, 'Silver', 5, 11, 'Ag'),
            Element(48, 'Cadmium', 5, 12, 'Cd'),
            Element(49, 'Induium', 5, 13, 'In'),
            Element(50, 'Tin', 5, 14, 'Sn'),
            Element(51, 'Antimony', 5, 15, 'Sb'),
            Element(52, 'Tellurium', 5, 16, 'Te'),
            Element(53, 'Iodine', 5, 17, 'I'),
            Element(54, 'Xenon', 5, 18, 'Xe'),
            # 6th period
            Element(55, 'Caesium', 6, 1, 'Cs'),
            Element(56, 'Barium', 6, 2, 'Ba'),
            Element(57, 'Lanthanum', 6, 3, 'La'),
            Element(72, 'Hafnium', 6, 4, 'Hf'),
            Element(73, 'Tantalum', 6, 5, 'Ta'),
            Element(74, 'Tungsten', 6, 6, 'W'),
            Element(75, 'Rhenium', 6, 7, 'Re'),
            Element(76, 'Osmium', 6, 8, 'Os'),
            Element(77, 'Iridium', 6, 9, 'Ir'),
            Element(78, 'Platinum', 6, 10, 'Pt'),
            Element(79, 'Gold', 6, 11, 'Au'),
            Element(80, 'Mercury', 6, 12, 'Hg'),
            Element(81, 'Thallium', 6, 13, 'Tl'),
            Element(82, 'Lead', 6, 14, 'Pb'),
            Element(83, 'Bismuth', 6, 15, 'Bi'),
            Element(84, 'Polonium', 6, 16, 'Po'),
            Element(85, 'Astatine', 6, 17, 'At'),
            Element(86, 'Radeon', 6, 18, 'Rn'),
            # 7th period
            Element(87, 'Francium', 7, 1, 'Fr'),
            Element(88, 'Radium', 7, 2, 'Ra'),
            Element(89, 'Actinium', 7, 3, 'Ac'),
            Element(104, 'Rutherfordium', 7, 4, 'Rf'),
            Element(105, 'Dubnium', 7, 5, 'Db'),
            Element(106, 'Seaborgium', 7, 6, 'Sg'),
            Element(107, 'Bohrium', 7, 7, 'Bh'),
            Element(108, 'Hassium', 7, 8, 'Hs'),
            Element(109, 'Meitnerium', 7, 9, 'Mt'),
            Element(110, 'Damstadium', 7, 10, 'Ds'),
            Element(111, 'Roentgenium', 7, 11, 'Rg'),
            Element(112, 'Copernicium', 7, 12, 'Cn'),
            Element(113, 'Nihonium', 7, 13, 'Nh'),
            Element(114, 'Flerovium', 7, 14, 'Fl'),
            Element(115, 'Moscovium', 7, 15, 'Mc'),
            Element(116, 'Livermorium', 7, 16, 'Lv'),
            Element(117, 'Tennessine', 7, 17, 'Ts'),
            Element(118, 'Oganesson', 7, 18, 'Og')
        )

    def get_by_atomic_number(self, number):
        if number > 57:
            for element in self.table[57:]:
                if element.atomic_number == number:
                    return element

        else:
            return self.table[number-1]

    def get_by_name(self, name):
        for element in self.table:
            if element.name.lower() == name.lower():
                return element

    def get_by_placement(self, period, group):
        for element in self.table:
            if element.period == period and element.group == group:
                return element

    def get_by_symbol(self, symbol):
        for elemnt in self.table:
            if elemnt.symbol == symbol:
                return elemnt

    def get_left_or_right(self, element_a, element_b):
        if element_a and element_b:
            if element_a.group > element_b.group:
                return "right"
            elif element_a.group < element_b.group:
                return "left"