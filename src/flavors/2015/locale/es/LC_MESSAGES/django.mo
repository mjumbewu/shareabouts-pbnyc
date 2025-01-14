��    x      �  �   �      (
  G  )
  �  q  >  ^  g  �       
        '     E     I     O  ;  e  B   �      �      �   *   !  5   <!  I   r!  
   �!  =   �!     "     ""     *"     9"      X"     y"     �"  	   �"     �"     �"  �   �"  	   �#     �#     �#  "   �#     �#     $  k   1$  �   �$  =   v%     �%  
   �%     �%     �%     	&     $&     :&     B&     b&  �   x&  ^   4'     �'     �'     �'  /   �'  !   (     ((     5(     H(  7   ](  /   �(     �(     �(     �(  E   )  
   N)     Y)     k)     y)     �)     �)     �)     �)  $   �)     �)  (   *  $   4*     Y*     j*     ~*  2   �*     �*     �*     �*     �+     �+     �+     ,     ,     $,     ,,     @,     V,  ?   e,     �,     �,     �,  �   �,  �   �-     &.     ..     G.     b.  	   x.      �.  	   �.  4   �.  6   �.  7   /  -   Q/  =   /  9   �/     �/     �/     0     0  	   0     %0  	   -0     70  �  @0  �  2  �  8  �  �:  h  �@     YF     oF  )   xF     �F     �F  %   �F  w  �F  T   JH     �H     �H  >   �H  S   I  L   hI     �I  I   �I  '   J  
   3J     >J  '   GJ  (   oJ     �J     �J     �J     �J     �J  @  �J     L     &L     @L  '   NL  "   vL  4   �L  f   �L  �   5M  V   3N     �N     �N  -   �N     �N  $   �N     O  	   =O     GO     fO  �   �O  f   nP     �P  #   �P     Q  J   +Q  -   vQ     �Q     �Q     �Q  ?   �Q  ;   R  !   XR     zR     �R  R   �R     �R     S     S     +S  '   >S     fS     sS     S  *   �S  $   �S  .   �S     T     .T     MT     cT  A   yT     �T     �T    �T     �U     V     V     #V     ;V      CV     dV     tV     �V  ^   �V     �V  #   �V     !W  �   7W  �   X  
   �X     �X     �X      Y     6Y  $   EY  	   jY  /   tY  ?   �Y  2   �Y  /   Z  ?   GZ  9   �Z     �Z  
   �Z     �Z     �Z     �Z     �Z     �Z     [     a       ?       o       	   P   R   k       t   m   D                  Z              
   "           r       -           G               :      i       '   3   L   8   \      S   M              B       X   *   ;   0   ,      O                    [   T   =   N                            j       _          +      (   c   l       ]   /      h   g   !   V   9   6       <           d          F   U      e   `   &   x      q      w   1   n      W   )       2      .   $      A   #   %           >          4   f   Y   H       J      u   p           E   K   ^   s   5   I         @   Q   7         C       b       v        

        {{#if place.source}}
        A new <span class="place-type">{{   place.place_type_label }} idea </span>from <strong>{{ place.source }}</strong>{{#if place.CounDist}} in District {{ place.CounDist }}{{/if}} named <span class="place-name">{{ place.name }}</span>

        {{^}}
          <strong>
          {{#if target.submitter}}
            <img src="{{ target.submitter.avatar_url }}" class="avatar" /> {{ target.submitter.name }}
          {{^}}
            <!-- TODO: FIXME: don't hardcode image URL -->
            <img src="/static/css/images/user-50.png" class="avatar" /> {{ target.submitter_name }}
          {{/if}}
          </strong>
    
          {{#if is_place }}
            {{ action }} a{{#if place.type_starts_with_vowel }}n{{/if }} <span class="place-type">{{     place.place_type_label }} idea </span>
            {{#if place.CounDist}} in District {{ place.CounDist }}{{/if}}
            {{#if place.name }}
              named <span class="place-name">{{ place.name }}</span>
            {{^}}
              {{#if place.location }}
                at <span class="place-name">{{>location-string place.location }}</span>
              {{/if }}
            {{/if }}
          {{else}}
            {{ action }}
    
            {{#if place.name }}
              <span class="place-name">{{ place.name }}</span>
            {{else}}
              a{{# place.type_starts_with_vowel }}n{{/ place.type_starts_with_vowel }} {{ place.    place_type_label }}
            {{/if }}
            {{#if place.CounDist}} in District {{ place.CounDist }}{{/if}}
          {{/if }}
           

        {{#if source}}
          A {{place_type_label location_type }} idea {{#if CounDist}} in District {{ CounDist }}{{/if}} from <strong>{{ source }}</strong>
        {{^}}
        <strong class="point-submitter">
          {{#if submitter}}
            <img src="{{ submitter.avatar_url }}" class="avatar" /> {{ submitter.name }}
          {{^}}
            <!-- TODO: FIXME: don't hardcode image URL -->
            <img src="/static/css/images/user-50.png" class="avatar" /> {{ submitter_name }}
          {{/if}}
            </strong> suggested this {{place_type_label location_type }} idea {{#if CounDist}} in District {{ CounDist }}{{/if}}. 
        {{/if}}
            <p><small>Near {{>location-string location }}</small></p>

         
        {{#if place.source}}
        A new <span class="place-type">{{   place.place_type_label }} idea </span>from <strong>{{ place.source }}</strong>{{#if place.CounDist}} in District {{ place.CounDist }}{{/if}} named <span class="place-name">{{ place.name }}</span>

        {{^}}
          <strong>
          {{#if target.submitter}}
            <img src="{{ target.submitter.avatar_url }}" class="avatar" /> {{ target.submitter.name }}
          {{^}}
            <!-- TODO: FIXME: don't hardcode image URL -->
            <img src="/static/css/images/user-50.png" class="avatar" /> {{ target.submitter_name }}
          {{/if}}
          </strong>
  
          {{#if is_place }}
            {{ action }} a{{#if place.type_starts_with_vowel }}n{{/if }} <span class="place-type">{{   place.place_type_label }} idea </span>
            {{#if place.CounDist}} in District {{ place.CounDist }}{{/if}}
            {{#if place.name }}
              named <span class="place-name">{{ place.name }}</span>
            {{^}}
              {{#if place.location }}
                at <span class="place-name">{{>location-string place.location }}</span>
              {{/if }}
            {{/if }}
          {{else}}
            {{ action }}
  
            {{#if place.name }}
              <span class="place-name">{{ place.name }}</span>
            {{else}}
              a{{# place.type_starts_with_vowel }}n{{/ place.type_starts_with_vowel }} {{ place.  place_type_label }}
            {{/if }}
            {{#if place.CounDist}} in District {{ place.CounDist }}{{/if}}
          {{/if }}
           
  {{#if shortlisted }}
    <p><strong>Location</strong>: {{ Location }}</p>
    <p><strong>Description</strong>: {{ description }}</p>
    <p><strong>Cost</strong>: {{ Cost }}</p>
    <p>Vote for this project between March 29th and April 6th. <a href="http://pbnyc.org/" title="Participatory Budgeting in New York City | REAL MONEY. REAL PROJECTS. REAL POWER.">Find out how and where</a>.</p>
  {{ else }}
    {{#if year }} <!-- it's a manually-added project from previous years -->
      <p class="description">{{ description }}</p>
    
      {{#if status }}
        <p><strong>Status</strong>: {{ status }} {{#if updated }} (last updated {{ updated }}) {{/if }}</p>
      {{/if }}

      <p><strong>Cost</strong>: {{ cost }}</p>
      {{#if agency}}<p><strong>Agency</strong>: {{ agency }}</p> {{/if}}
    
    {{ else }}
  
      {{#if name }} <p>My project idea is: <span class="idea-title">{{ name }}</span></p> {{/if }}

      {{#if description }} <p>So that people could: {{ description }}</p> {{/if }}
  
      {{# attachments }}
        <div class="place-item place-attachment-{{ name }}">
          <img src="{{ file }}" class="place-value place-value-{{ name }}" alt="{{ name }}">
        </div>
      {{/ attachments }}

    {{/if }}
  {{/if }}
  
  {{^if survey_config}}
    <a href="/place/{{ id }}" class="view-on-map-btn btn btn-small">View On Map</a>
  {{/if}}
  
  Schools and Education (Expenses) (Outside of the PB districts) ... About After school programs After you submit your idea on this Idea Collection Map, your idea will be given to community volunteers, called Budget Delegates. Budget Delegates work in your district to turn ideas into real proposals for a ballot, with input from city agencies. These proposals will be up for a community-wide vote in the spring. All ideas must be submitted by <strong>November 16, 2015</strong>. Anyone can post ideas. Approximate location: Basketball court, park benches, skate park Build a wheelchair accessible ramp, improved lighting Buy lighting, sound, or other equipment for a local cultural organization Categories Check out the guidelines</a> to see what ideas can be funded. Choose Your Council District Comment Council Member Culture & Community Facilities Culture and Community Facilities Describe your idea District Districts Educational programs Eligible Eligible ideas must be for "capital" projects: physical infrastructure for public benefit, such as park improvements or new technology for schools. “Expense" projects, such as afterschool programs or expanding bus service, are not eligible. Eligible: Enter an address... Environment Examples of Eligible Capital Ideas Expanding bus service Extending library staff hours For example, "Build a wheelchair accessible ramp, improved lighting" or "Weatherization of public housing". For more information on participatory budgeting, other community PB events like Neighborhood Assemblies, and how to get more involved, visit <a href="http://council.nyc.gov/PB" target="_blank">council.nyc.gov/PB</a>. Green infrastructure such as bioswales and permeable pavement Green roofs on schools Guidelines Hiring home health care workers Hiring more police Hiring nurses for a clinic Hiring security staff Housing How would YOU spend $1 Million? I'd like to volunteer Ideas must be "capital" projects - building, installing, or repairing something for public benefit, such as renovating a public basketball court or purchasing new computers for a library. If you have an idea about how things could work better in your community, share it on the map. Leave a Comment Make bathrooms ADA compliant My project idea is... New York City Council's Participatory Budgeting New computers for a local library Non-Eligible Parks & Recreation Parks and Recreation Paying bills for electricity of a public building, etc. Pedestrian safety improvements at intersections Pick a category for your idea Playground upgrades Please choose... Please note that the input period for this district is over for 2015. Powered by Previously funded Public Health Public Safety Public exercise equipment Real Money. Real Power. Real Projects. Renovation of local community center Renovation of school property Renovations for local hospital or clinic Repairs to privately-owned sidewalks Road resurfacing Schools & Education Schools and Education Security cameras around schools and public housing Seniors Share my idea Share your ideas on the map for how things could be better in your community. <a href="/page/guidelines" title="Participatory Budgeting in New York City | REAL MONEY. REAL PROJECTS. REAL POWER.">Check out the guidelines</a> to see what ideas can be funded. Show All Show as a list Show on a map So that people could... Someone Speaker Streets & Sidewalks Streets and Sidewalks Submit an idea Subway station improvements such as installation of help points Support This! Tech for public school Technology centers Through Participatory Budgeting, community members - like you - directly decide how to spend at least $1,000,000 of the public budget in participating Council District. To add a spot, drag the map until the crosshairs are over the desired location. Ideas will be considered by the Council District within which they are located. Transit Transit & Transportation Transit and Transportation Upgrade public plazas Volunteer Weatherization of public housing Your Name Your age (optional and will NOT be shown on the map) Your email (required and will NOT be shown on the map) Your gender (optional and will NOT be shown on the map) Your name (required and will be shown on map) Your phone number (optional and will NOT be shown on the map) Your zip code (optional and will NOT be shown on the map) Youth comment commented on comments suggested support supported supports Project-Id-Version: Shareabouts PBNYC 2015/16
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2015-10-07 12:46-0400
PO-Revision-Date: 2015-10-08 04:01+0000
Last-Translator: Ivan Luevanos <ILuevanos@council.nyc.gov>
Language-Team: Spanish (http://www.transifex.com/mjumbewu/shareabouts-pbnyc-201516/language/es/)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: es
Plural-Forms: nplurals=2; plural=(n != 1);
 

        {{#if place.source}}
        Una nueva idea de <span class="place-type">{{   place.place_type_label }} </span>de <strong>"{{ place.source }}"</strong>{{#if place.CounDist}} en el Distrito {{ place.CounDist }}{{/if}} nombrada <span class="place-name">"{{ place.name }}"</span>

        {{^}}
          <strong>
          {{#if target.submitter}}
            <img src="{{ target.submitter.avatar_url }}" class="avatar" /> {{ target.submitter.name }}
          {{^}}
            <!-- TODO: FIXME: don't hardcode image URL -->
            <img src="/static/css/images/user-50.png" class="avatar" /> {{ target.submitter_name }}
          {{/if}}
          </strong>
    
          {{#if is_place }}
            {{ action }} una idea de <span class="place-type">{{     place.place_type_label }} </span>
            {{#if place.CounDist}} en el Distrito {{ place.CounDist }}{{/if}}
            {{#if place.name }}
              nombrada <span class="place-name">"{{ place.name }}"</span>
            {{^}}
              {{#if place.location }}
                en <span class="place-name">{{>location-string place.location }}</span>
              {{/if }}
            {{/if }}
          {{else}}
            {{ action }}
    
            {{#if place.name }}
              <span class="place-name">"{{ place.name }}"</span>
            {{else}}
              una idea de {{ place.    place_type_label }}
            {{/if }}
            {{#if place.CounDist}} en el Distrito {{ place.CounDist }}{{/if}}
          {{/if }}
           

        {{#if source}}
          Una idea de {{place_type_label location_type }} {{#if CounDist}} en Distrito {{ CounDist }}{{/if}} de <strong>"{{ source }}"</strong>
        {{^}}
        <strong class="point-submitter">
          {{#if submitter}}
            <img src="{{ submitter.avatar_url }}" class="avatar" /> {{ submitter.name }}
          {{^}}
            <!-- TODO: FIXME: don't hardcode image URL -->
            <img src="/static/css/images/user-50.png" class="avatar" /> {{ submitter_name }}
          {{/if}}
            </strong> sugerió esta idea de {{place_type_label location_type }} {{#if CounDist}} en Distrito {{ CounDist }}{{/if}}. 
        {{/if}}
            <p><small>Cerca de {{>location-string location }}</small></p>

         
        {{#if place.source}}
        Una idea nueva de <span class="place-type">{{   place.place_type_label }}</span> de <strong>"{{ place.source }}"</strong>{{#if place.CounDist}} en el Distrito {{ place.CounDist }}{{/if}} nombrada <span class="place-name">"{{ place.name }}"</span>

        {{^}}
          <strong>
          {{#if target.submitter}}
            <img src="{{ target.submitter.avatar_url }}" class="avatar" /> {{ target.submitter.name }}
          {{^}}
            <!-- TODO: FIXME: don't hardcode image URL -->
            <img src="/static/css/images/user-50.png" class="avatar" /> {{ target.submitter_name }}
          {{/if}}
          </strong>
  
          {{#if is_place }}
            {{ action }} una idea de <span class="place-type">{{   place.place_type_label }} </span>
            {{#if place.CounDist}} en el Distrito {{ place.CounDist }}{{/if}}
            {{#if place.name }}
              nombrada <span class="place-name">"{{ place.name }}"</span>
            {{^}}
              {{#if place.location }}
                en <span class="place-name">{{>location-string place.location }}</span>
              {{/if }}
            {{/if }}
          {{else}}
            {{ action }}
  
            {{#if place.name }}
              <span class="place-name">"{{ place.name }}"</span>
            {{else}}
              una idea de {{ place.  place_type_label }}
            {{/if }}
            {{#if place.CounDist}} en el Distrito {{ place.CounDist }}{{/if}}
          {{/if }}
           
  {{#if shortlisted }}
    <p><strong>Ubicación</strong>: {{ Location }}</p>
    <p><strong>Idea</strong>: {{ description }}</p>
    <p><strong>Costo</strong>: {{ Cost }}</p>
    <p>Vote for this project between March 29th and April 6th. <a href="http://pbnyc.org/" title="Participatory Budgeting in New York City | REAL MONEY. REAL PROJECTS. REAL POWER.">Find out how and where</a>.</p>
  {{ else }}
    {{#if year }} <!-- it's a manually-added project from previous years -->
      <p class="description">{{ description }}</p>
    
      {{#if status }}
        <p><strong>Estatus</strong>: {{ status }} {{#if updated }} (last updated {{ updated }}) {{/if }}</p>
      {{/if }}

      <p><strong>Costo</strong>: {{ cost }}</p>
      {{#if agency}}<p><strong>Agencia</strong>: {{ agency }}</p> {{/if}}
    
    {{ else }}
  
      {{#if name }} <p>Mi idea es: <span class="idea-title">"{{ name }}"</span></p> {{/if }}

      {{#if description }} <p>Para que la gente pueda: "{{ description }}"</p> {{/if }}
  
      {{# attachments }}
        <div class="place-item place-attachment-{{ name }}">
          <img src="{{ file }}" class="place-value place-value-{{ name }}" alt="{{ name }}">
        </div>
      {{/ attachments }}

    {{/if }}
  {{/if }}
  
  {{^if survey_config}}
    <a href="/place/{{ id }}" class="view-on-map-btn btn btn-small">Ver en el mapa</a>
  {{/if}}
  
 Escuelas y Educación (Gastos) (Fuera de los Distritos PP participantes) ... Sobre Programas Despues del Horario Escolar Después que entregue su idea en este mapa de ideas, su idea sera entregada a voluntarios comunitarios llamados delegados del presupuesto. Los delegados del presupuesto trabajan en su distrito para convertir sus ideas en propuestas concretas para una boleta, con la ayuda de agencias municipales. Estas propuestas estarán listas para la semana de votación en la primavera.  Todas las ideas deben ser sometidas antes del <strong>16 de Noviembre del </strong>. Cualquiera puede sugerir ideas Ubicación aproximada: Cancha de baloncesto, bancas en el parque, parque para patinar Construir infraestructuras aptas para personas discapacitadas, mejorar iluminación Comprar equipos de iluminación, audio para una organización cultural local Categorías Revise los reglamentos</a> para ver cuáles ideas pueden ser financiadas. Elija su distrito del Concejo Municipal Comentario Concejal Instalaciones comunitarias y culturales Instalaciones comunitarias y culturales  Describe tu idea Distrito Distrito Programas educacionales Elegible Las ideas elegibles deben ser para proyectos de "capital": la infraestructura física para el beneficio público, como las mejoras de parques o nuevas tecnologías para las escuelas. Proyectos de "gastos", tales como los programas despues del horario escolar o la ampliación del servicio de autobuses, no son elegibles. Elegible Escriba una dirección... Medioambiente Ejemplos de ideas capitales calificadas Ampliar los servicios de autobuses Extender las horas para el personal de la biblioteca Por ejemplo, Construir una rampa accesible para silla de ruedas o Climatización en Viviendas Publicas Para obtener más información sobre el presupuesto participativo, otros eventos comunales de la PP, como Asambleas Comunales , y cómo te puedes envolver  más , visite <a href="http://council.nyc.gov/PB" target="_blank"> council.nyc . </a> gov / PB .  Infraestructura verde tal como canales de filtración biológico y pavimento permeable Techos verdes en las escuelas Reglamentos   Emplear trabajadores de la salud en el hogar Emplear más policías Emplear enfermeras para una clínica Emplear personal de seguridad Viviendas ¿Cómo gastarías $1 millón? Me gustaría ser voluntario Las ideas deben ser proyectos de "capital":  construcción, instalación o reparación de algo para el beneficio público, como la renovación de una cancha de baloncesto pública o la compra de nuevas computadoras para una biblioteca. Si tiene una idea de cómo las cosas podrían funcionar mejor en su comunidad, compártalo en el mapa. Deje un comentario Hacer que baños cumplan con la ADA Mi idea para un proyecto es... Presupuesto Participativo del Concejo Municipal de la Ciudad de Nueva York Nuevas computadoras para una biblioteca local No elegible Parques y Recreación Parques y Recreación Pagar las cuentas de electricidad de un edificio público, etc. Mejoras la seguridad para peatones en las  intersecciones   Elija una categoría para tu idea Mejoramiento de areas de recreo Elija... Tenga en cuenta que el periodo para someter su idea en este distrito ha terminado. Potenciado por Previamente financiado Salud pública Seguridad pública Equipo de ejercicios para el público   Dinero Real. Poder Real. Proyectos Reales Renovación de un centro comunitario local Renovación de propiedades escolares Renovaciones para un hospital local o clínica Reparaciones a aceras privadas Repavimentación de carreteras Escuelas y educación Escuelas y educación Cámaras de seguridad alrededor de escuelas y viviendas públicas Personas mayores Comparte mi idea  Comparta sus ideas en el mapa para ver como cosas podrían ser mejoradas en su comunidad.<a href="/page/guidelines" title="Participatory Budgeting in New York City | REAL MONEY. REAL PROJECTS. REAL POWER."> Revise los reglamentos </a> para ver cuales ideas pueden ser financiadas.  Mostrar Todo Ver como lista Ver en el mapa Para que gente pueda... Alguien Presidenta del Concejo Municipal Calles y aceras Calles y aceras Someter una idea Mejoramiento de las estaciones del tern subterráneo como  la instalación de puntos de ayuda. ¡Apoye! Tecnología para escuelas públicas Centros tecnológicos A través del Presupuesto Participativo, miembros de la comunidad - como tú - deciden directamente cómo gastar al menos $ 1.000.000 del presupuesto público en  Distritos participantes  del  Concejo Municipal. Para añadir un punto, arrastre el mapa hasta que la cruz del cursor se encuentre sobre la ubicación deseada. Las ideas serán consideradas por el distrito del Concejo Municipal en el que se encuentran. Transporte Tránsito y transporte Tránsito y transportación Mejoramiento de plazas públicas Ser voluntario Climatización de  vivienda pública Tu nombre Su edad (opcional y NO se mostrará en el mapa) Su correo electrónico (requerido y no se mostrará en el mapa) Su género (opcional y NO se mostrará en el mapa) Su nombre (requerido y se mostrará en el mapa) Su número de teléfono (opcional y NO se mostrará en el mapa) Su código postal (opcional y NO se mostrará en el mapa) Jóvenes comentario comentó sobre comentarios sugerido Apoyo apoyado por  Apoya 