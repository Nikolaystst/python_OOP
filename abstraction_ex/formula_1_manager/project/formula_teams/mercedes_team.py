from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    expenses = 200_000
    sponsors = {"Petronas": {1: 1_000_000, 3: 500_000}, "TeamViewer": {5: 100_000, 7: 50_000}}

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        sponsorship = 0
        for sponsor, val in MercedesTeam.sponsors.items():
            for place, prize in val.items():
                if place >= race_pos:
                    sponsorship += prize
                    break

        sponsorship -= MercedesTeam.expenses
        self.budget += sponsorship
        return f"The revenue after the race is {sponsorship}$. Current budget {self.budget}$"
