test = {
  'name': 'Question 3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Ensure your correlation function returns one number between -1 and 1
          >>> abs(correlation(Table().with_columns('a', np.random.normal(0, 1, 10),'b', np.random.normal(0, 1, 10)))) <= 1
          True
          >>> np.allclose(standard_units(np.arange(5)), np.sqrt(2)/2 * np.arange(-2, 3))
          True
          >>> np.allclose(correlation(faithful), 0.3727822255707511)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
