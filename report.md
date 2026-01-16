# Peppol Schematron Change Report - Version v3.0.0

## Schematron Changes
- [MoveNode] MoveNode(node='/*/*/*[1]', target='/*/*[1]', position=1)
- [UpdateAttrib] UpdateAttrib(node='/*/*/*[1]', name='context', value='cbc:ID')
- [UpdateAttrib] UpdateAttrib(node='/*/*/*[2]', name='context', value='cbc:NewField')
- [UpdateAttrib] UpdateAttrib(node='/*/*/*[1]/*[1]', name='test', value='string-length(.) > 5')
- [UpdateTextIn] UpdateTextIn(node='/*/*/*[1]/*[1]', text='ID must be at least 5 chars')
- [UpdateTextIn] UpdateTextIn(node='/*/*/*[2]/*[1]', text='NewField is required')

## Mapping Impact Analysis
- **WARNING**: order_mapping.json (Field: cbc:ID) - Schematron rule changed for ID field.