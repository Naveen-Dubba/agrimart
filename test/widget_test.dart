import 'package:flutter_test/flutter_test.dart';
import 'package:agrimart/main.dart';

void main() {
  testWidgets('App smoke test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const AgrimartApp());

    // Verify that the 'Welcome 🌿' text exists on the login screen
    expect(find.text('Welcome 🌿'), findsOneWidget);
  });
}
