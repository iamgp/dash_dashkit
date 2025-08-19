export interface ContributionDay {
  date: string;
  count: number;
}

export interface ContributionData {
  contributions: ContributionDay[];
  total?: number;
}