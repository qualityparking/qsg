if (role == 'member') {
  Navigator.pushReplacement(
    context,
    MaterialPageRoute(builder: (_) => const MemberDashboard()),
  );
} else if (role == 'petugas') {
  Navigator.pushReplacement(
    context,
    MaterialPageRoute(builder: (_) => const DashboardPetugasScreen()),
  );
}
