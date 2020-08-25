// https://www.hackerrank.com/challenges/js10-date/problem
function getDayName(dateString) {
  let dayName;
  let d = new Date(dateString).getDay();
  const days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  dayName = days[d];
  return dayName;
}
