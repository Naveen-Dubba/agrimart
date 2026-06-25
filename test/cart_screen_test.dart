import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:agrimart/screens/cart_screen.dart';

void main() {
  Widget createWidgetUnderTest() {
    return const MaterialApp(
      home: CartScreen(),
    );
  }

  group('CartScreen Tests', () {
    testWidgets('renders CartScreen with correct title', (WidgetTester tester) async {
      await tester.pumpWidget(createWidgetUnderTest());

      expect(find.text('My Cart'), findsOneWidget);
    });

    testWidgets('displays all initial cart items', (WidgetTester tester) async {
      await tester.pumpWidget(createWidgetUnderTest());

      expect(find.text('Professional Pruning Shears'), findsOneWidget);
      expect(find.text('Bright Orange Chainsaw'), findsOneWidget);
      expect(find.text('Backpack Garden Sprayer'), findsOneWidget);
    });

    testWidgets('displays correct initial total amount', (WidgetTester tester) async {
      await tester.pumpWidget(createWidgetUnderTest());

      // 1660*1 + 12500*1 + 3200*2 = 20560
      expect(find.text('₹20560'), findsOneWidget);
    });

    testWidgets('renders add and remove quantity buttons', (WidgetTester tester) async {
      await tester.pumpWidget(createWidgetUnderTest());

      // 3 items in the cart, so 3 add and 3 remove buttons
      expect(find.byIcon(Icons.add_circle_outline), findsNWidgets(3));
      expect(find.byIcon(Icons.remove_circle_outline), findsNWidgets(3));
    });

    testWidgets('renders checkout button', (WidgetTester tester) async {
      await tester.pumpWidget(createWidgetUnderTest());

      expect(find.text('CHECKOUT'), findsOneWidget);
    });
  });
}
